from __future__ import annotations

import ast
import operator as op
import tkinter as tk
from tkinter import ttk


class CalcError(Exception):
    pass


_BIN_OPS: dict[type[ast.operator], object] = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.FloorDiv: op.floordiv,
    ast.Mod: op.mod,
    ast.Pow: op.pow,
}

_UNARY_OPS: dict[type[ast.unaryop], object] = {
    ast.UAdd: op.pos,
    ast.USub: op.neg,
}


def _eval(node: ast.AST) -> float:
    if isinstance(node, ast.Expression):
        return _eval(node.body)

    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return float(node.value)
        raise CalcError("Only numbers are allowed.")

    if isinstance(node, ast.BinOp):
        fn = _BIN_OPS.get(type(node.op))
        if fn is None:
            raise CalcError("Operator not allowed.")
        left = _eval(node.left)
        right = _eval(node.right)
        try:
            return float(fn(left, right))
        except ZeroDivisionError as e:
            raise CalcError("Division by zero.") from e

    if isinstance(node, ast.UnaryOp):
        fn = _UNARY_OPS.get(type(node.op))
        if fn is None:
            raise CalcError("Unary operator not allowed.")
        return float(fn(_eval(node.operand)))

    if isinstance(node, (ast.Call, ast.Name, ast.Attribute, ast.Subscript, ast.List, ast.Tuple, ast.Dict)):
        raise CalcError("Only math expressions are allowed.")

    raise CalcError("Unsupported expression.")


def evaluate(expr: str) -> float:
    expr = expr.strip()
    if not expr:
        raise CalcError("Enter an expression.")
    try:
        tree = ast.parse(expr, mode="eval")
    except SyntaxError as e:
        raise CalcError("Invalid expression.") from e
    return _eval(tree)


class CalculatorApp(ttk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master, padding=12)
        self.master = master

        self.expr = tk.StringVar(value="")
        self.result = tk.StringVar(value="")

        self._build()
        self._bind_keys()

    def _build(self) -> None:
        self.master.title("Calculator")
        self.master.minsize(360, 460)

        style = ttk.Style(self.master)
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        entry = ttk.Entry(self, textvariable=self.expr, font=("Segoe UI", 16))
        entry.grid(row=0, column=0, columnspan=4, sticky="ew", ipady=8)
        entry.focus_set()

        result = ttk.Label(self, textvariable=self.result, anchor="e", font=("Segoe UI", 13))
        result.grid(row=1, column=0, columnspan=4, sticky="ew", pady=(8, 10))

        for c in range(4):
            self.columnconfigure(c, weight=1)
        self.rowconfigure(2, weight=1)

        buttons = [
            ("C", self.clear),
            ("⌫", self.backspace),
            ("(", lambda: self.append("(")),
            (")", lambda: self.append(")")),
            ("7", lambda: self.append("7")),
            ("8", lambda: self.append("8")),
            ("9", lambda: self.append("9")),
            ("/", lambda: self.append("/")),
            ("4", lambda: self.append("4")),
            ("5", lambda: self.append("5")),
            ("6", lambda: self.append("6")),
            ("*", lambda: self.append("*")),
            ("1", lambda: self.append("1")),
            ("2", lambda: self.append("2")),
            ("3", lambda: self.append("3")),
            ("-", lambda: self.append("-")),
            ("0", lambda: self.append("0")),
            (".", lambda: self.append(".")),
            ("**", lambda: self.append("**")),
            ("+", lambda: self.append("+")),
            ("//", lambda: self.append("//")),
            ("%", lambda: self.append("%")),
            ("=", self.calculate),
        ]

        grid = ttk.Frame(self)
        grid.grid(row=2, column=0, columnspan=4, sticky="nsew")
        for r in range(6):
            grid.rowconfigure(r, weight=1)
        for c in range(4):
            grid.columnconfigure(c, weight=1)

        def add_btn(text: str, cmd, r: int, c: int, cs: int = 1) -> None:
            b = ttk.Button(grid, text=text, command=cmd)
            b.grid(row=r, column=c, columnspan=cs, sticky="nsew", padx=4, pady=4, ipadx=6, ipady=6)

        add_btn("C", self.clear, 0, 0)
        add_btn("⌫", self.backspace, 0, 1)
        add_btn("(", lambda: self.append("("), 0, 2)
        add_btn(")", lambda: self.append(")"), 0, 3)

        add_btn("7", lambda: self.append("7"), 1, 0)
        add_btn("8", lambda: self.append("8"), 1, 1)
        add_btn("9", lambda: self.append("9"), 1, 2)
        add_btn("/", lambda: self.append("/"), 1, 3)

        add_btn("4", lambda: self.append("4"), 2, 0)
        add_btn("5", lambda: self.append("5"), 2, 1)
        add_btn("6", lambda: self.append("6"), 2, 2)
        add_btn("*", lambda: self.append("*"), 2, 3)

        add_btn("1", lambda: self.append("1"), 3, 0)
        add_btn("2", lambda: self.append("2"), 3, 1)
        add_btn("3", lambda: self.append("3"), 3, 2)
        add_btn("-", lambda: self.append("-"), 3, 3)

        add_btn("0", lambda: self.append("0"), 4, 0)
        add_btn(".", lambda: self.append("."), 4, 1)
        add_btn("**", lambda: self.append("**"), 4, 2)
        add_btn("+", lambda: self.append("+"), 4, 3)

        add_btn("//", lambda: self.append("//"), 5, 0)
        add_btn("%", lambda: self.append("%"), 5, 1)
        add_btn("=", self.calculate, 5, 2, cs=2)

        help_text = "Ops: +  -  *  /  //  %  **    Enter = calculate"
        help_lbl = ttk.Label(self, text=help_text, foreground="#555")
        help_lbl.grid(row=3, column=0, columnspan=4, sticky="ew", pady=(10, 0))

        self.grid(sticky="nsew")
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

    def _bind_keys(self) -> None:
        self.master.bind("<Return>", lambda _e: self.calculate())
        self.master.bind("<KP_Enter>", lambda _e: self.calculate())
        self.master.bind("<Escape>", lambda _e: self.clear())

    def append(self, s: str) -> None:
        self.expr.set(self.expr.get() + s)
        self.result.set("")

    def clear(self) -> None:
        self.expr.set("")
        self.result.set("")

    def backspace(self) -> None:
        cur = self.expr.get()
        self.expr.set(cur[:-1])
        self.result.set("")

    def calculate(self) -> None:
        try:
            value = evaluate(self.expr.get())
        except CalcError as e:
            self.result.set(f"Error: {e}")
            return
        if value.is_integer():
            self.result.set(str(int(value)))
        else:
            self.result.set(str(value))


def main() -> None:
    root = tk.Tk()
    root.geometry("380x520")
    CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

