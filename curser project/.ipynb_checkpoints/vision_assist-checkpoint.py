"""
Vision Assist Mode — Accessibility app for visually impaired users.

Features:
  - Reads text aloud (text-to-speech)
  - Detects obstacles using camera
  - Gives audio/vibration alerts
"""

from __future__ import annotations

import argparse
import queue
import sys
import threading
import time

try:
    import cv2
    import numpy as np
except ImportError:
    print("Install OpenCV: pip install opencv-python numpy")
    sys.exit(1)

try:
    import pyttsx3
except ImportError:
    print("Install pyttsx3: pip install pyttsx3")
    sys.exit(1)

# Optional: vibration on supported platforms (mobile/tablet)
# On Windows PC, we use audio beeps as the primary alert
try:
    import winsound
    HAS_WINSOUND = True
except ImportError:
    HAS_WINSOUND = False

try:
    import pytesseract
    HAS_OCR = True
except ImportError:
    HAS_OCR = False


# ---------------------------------------------------------------------------
# Text-to-Speech
# ---------------------------------------------------------------------------


class TextToSpeech:
    """Reads text aloud using system TTS."""

    def __init__(self, rate: int = 175, volume: float = 1.0) -> None:
        self._engine = pyttsx3.init()
        self._engine.setProperty("rate", rate)
        self._engine.setProperty("volume", volume)
        self._queue: queue.Queue[str | None] = queue.Queue()
        self._running = True
        self._thread = threading.Thread(target=self._worker, daemon=True)
        self._thread.start()

    def _worker(self) -> None:
        while self._running:
            try:
                text = self._queue.get(timeout=0.5)
                if text is None:
                    break
                self._engine.say(text)
                self._engine.runAndWait()
            except queue.Empty:
                continue

    def speak(self, text: str) -> None:
        if text.strip():
            self._queue.put(text.strip())

    def stop(self) -> None:
        self._running = False
        self._queue.put(None)
        self._thread.join(timeout=2)


# ---------------------------------------------------------------------------
# Obstacle Detection
# ---------------------------------------------------------------------------


class ObstacleDetector:
    """
    Detects obstacles in camera frames using edge/contour analysis.
    Splits the frame into left, center, right zones for directional alerts.
    """

    # Zone boundaries (fractions of frame width)
    LEFT_END = 0.33
    RIGHT_START = 0.66

    def __init__(self, threshold: float = 0.15, min_contour_area: int = 800) -> None:
        self.threshold = threshold
        self.min_contour_area = min_contour_area

    def _get_zones(self, frame: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        h, w = frame.shape[:2]
        left_w = int(w * self.LEFT_END)
        right_w = int(w * self.RIGHT_START)
        # Focus on lower half (walking path)
        lower_h = h // 2
        left = frame[lower_h:, :left_w]
        center = frame[lower_h:, left_w:right_w]
        right = frame[lower_h:, right_w:]
        return left, center, right

    def _zone_obstacle_score(self, zone: np.ndarray) -> float:
        gray = cv2.cvtColor(zone, cv2.COLOR_BGR2GRAY) if len(zone.shape) == 3 else zone
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blurred, 50, 150)
        contours, _ = cv2.findContours(
            edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        obstacle_area = sum(
            cv2.contourArea(c) for c in contours if cv2.contourArea(c) >= self.min_contour_area
        )
        total = zone.shape[0] * zone.shape[1]
        return min(1.0, obstacle_area / total) if total > 0 else 0.0

    def detect(self, frame: np.ndarray) -> tuple[float, float, float]:
        """Returns (left_score, center_score, right_score) in [0, 1]."""
        left, center, right = self._get_zones(frame)
        return (
            self._zone_obstacle_score(left),
            self._zone_obstacle_score(center),
            self._zone_obstacle_score(right),
        )


# ---------------------------------------------------------------------------
# Alerts (audio beeps / vibration)
# ---------------------------------------------------------------------------


def beep(freq: int = 880, duration: int = 80) -> None:
    """Play a short beep. Different patterns indicate direction."""
    if HAS_WINSOUND:
        try:
            winsound.Beep(freq, duration)
        except (ValueError, RuntimeError):
            pass


def alert_left() -> None:
    """One beep on left."""
    beep(600, 100)


def alert_center() -> None:
    """Two beeps for center (directly ahead)."""
    beep(880, 100)
    time.sleep(0.08)
    beep(880, 100)


def alert_right() -> None:
    """One beep on right."""
    beep(1000, 100)


# ---------------------------------------------------------------------------
# Main Vision Assist App
# ---------------------------------------------------------------------------


class VisionAssistApp:
    def __init__(
        self,
        camera_id: int = 0,
        alert_threshold: float = 0.12,
        speak_detection: bool = True,
    ) -> None:
        self.camera_id = camera_id
        self.alert_threshold = alert_threshold
        self.speak_detection = speak_detection
        self.tts = TextToSpeech()
        self.detector = ObstacleDetector()
        self._running = False
        self._last_alert = 0.0
        self._alert_cooldown = 1.2  # seconds between spoken alerts

    def _should_speak(self) -> bool:
        now = time.monotonic()
        if now - self._last_alert < self._alert_cooldown:
            return False
        self._last_alert = now
        return True

    def _handle_obstacles(self, left: float, center: float, right: float) -> None:
        triggered = []
        if left >= self.alert_threshold:
            triggered.append("left")
            alert_left()
        if center >= self.alert_threshold:
            triggered.append("center")
            alert_center()
        if right >= self.alert_threshold:
            triggered.append("right")
            alert_right()

        if triggered and self.speak_detection and self._should_speak():
            msg = "Obstacle " + " and ".join(triggered)
            self.tts.speak(msg)

    def run_obstacle_mode(self) -> None:
        """Run continuous obstacle detection with camera."""
        cap = cv2.VideoCapture(self.camera_id)
        if not cap.isOpened():
            self.tts.speak("Cannot open camera.")
            print("Error: Could not open camera.")
            return

        self.tts.speak("Vision Assist obstacle detection started. Point the camera ahead.")
        self._running = True

        try:
            while self._running:
                ret, frame = cap.read()
                if not ret:
                    break

                left, center, right = self.detector.detect(frame)
                self._handle_obstacles(left, center, right)

                # Check for quit key
                key = cv2.waitKey(1) & 0xFF
                if key == ord("q") or key == 27:
                    break
        finally:
            cap.release()
            cv2.destroyAllWindows()
            self._running = False
            self.tts.speak("Vision Assist stopped.")
            self.tts.stop()

    def read_text(self, text: str) -> None:
        """Read the given text aloud."""
        self.tts.speak(text)
        self.tts.stop()

    def run_scan_mode(self) -> None:
        """Use camera + OCR to read text from the environment aloud."""
        if not HAS_OCR:
            self.tts.speak("OCR not available. Install pytesseract and Tesseract.")
            print("Install: pip install pytesseract, and install Tesseract OCR")
            return

        cap = cv2.VideoCapture(self.camera_id)
        if not cap.isOpened():
            self.tts.speak("Cannot open camera.")
            return

        self.tts.speak("Point the camera at text. Press space to read, Q to quit.")
        self._running = True

        try:
            while self._running:
                ret, frame = cap.read()
                if not ret:
                    break

                cv2.imshow("Vision Assist - Scan Text", frame)
                key = cv2.waitKey(1) & 0xFF

                if key == ord(" "):
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    text = pytesseract.image_to_string(gray).strip()
                    if text:
                        self.tts.speak(text[:500])  # Limit length
                    else:
                        self.tts.speak("No text detected.")
                elif key == ord("q") or key == 27:
                    break
        finally:
            cap.release()
            cv2.destroyAllWindows()
            self.tts.stop()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Vision Assist Mode — Accessibility app for visually impaired users."
    )
    parser.add_argument(
        "mode",
        nargs="?",
        choices=["obstacle", "read", "scan"],
        default="obstacle",
        help="obstacle = camera obstacle detection; read = speak text (-t); scan = OCR from camera",
    )
    parser.add_argument(
        "-t", "--text",
        type=str,
        help="Text to read aloud (use with mode=read)",
    )
    parser.add_argument(
        "-c", "--camera",
        type=int,
        default=0,
        help="Camera device ID (default: 0)",
    )
    parser.add_argument(
        "--no-speak",
        action="store_true",
        help="Disable spoken obstacle alerts (beeps only)",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.12,
        help="Obstacle detection sensitivity 0.05–0.3 (default: 0.12)",
    )
    args = parser.parse_args()

    if args.mode == "read":
        app = VisionAssistApp()
        if args.text:
            app.read_text(args.text)
        else:
            app.read_text("No text provided. Use -t 'your text' to read aloud.")
        return

    if args.mode == "scan":
        app = VisionAssistApp(camera_id=args.camera)
        app.run_scan_mode()
        return

    app = VisionAssistApp(
        camera_id=args.camera,
        alert_threshold=args.threshold,
        speak_detection=not args.no_speak,
    )
    app.run_obstacle_mode()


if __name__ == "__main__":
    main()
