from __future__ import annotations

import ast
import operator as op
import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class CalcError(Exception):
    message: str

    def __str__(self) -> str:  # pragma: no cover
        return self.message


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
            raise CalcError("That operator is not allowed.")
        left = _eval(node.left)
        right = _eval(node.right)
        try:
            return float(fn(left, right))
        except ZeroDivisionError as e:
            raise CalcError("Division by zero.") from e

    if isinstance(node, ast.UnaryOp):
        fn = _UNARY_OPS.get(type(node.op))
        if fn is None:
            raise CalcError("That unary operator is not allowed.")
        return float(fn(_eval(node.operand)))

    if isinstance(node, ast.Call):
        raise CalcError("Function calls are not allowed.")

    if isinstance(node, ast.Name):
        raise CalcError("Variables are not allowed.")

    raise CalcError("Unsupported expression.")


def evaluate(expr: str) -> float:
    expr = expr.strip()
    if not expr:
        raise CalcError("Empty expression.")
    try:
        tree = ast.parse(expr, mode="eval")
    except SyntaxError as e:
        raise CalcError("Invalid expression syntax.") from e
    return _eval(tree)


def repl() -> int:
    print("Calculator (type 'exit' or 'quit' to leave)")
    print("Examples: 2+2, (3+4)*5, 2**8, 7//3, 7%3")
    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return 0

        if not line:
            continue
        if line.lower() in {"exit", "quit"}:
            return 0

        try:
            result = evaluate(line)
        except CalcError as e:
            print(f"Error: {e}")
            continue

        if result.is_integer():
            print(int(result))
        else:
            print(result)


def main(argv: list[str]) -> int:
    if len(argv) >= 2:
        expr = " ".join(argv[1:])
        try:
            result = evaluate(expr)
        except CalcError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 2
        if result.is_integer():
            print(int(result))
        else:
            print(result)
        return 0

    return repl()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

