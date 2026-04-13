"""Quick dependency-free calculus calculator.

Supported:
- f(x) evaluation
- numeric derivative at a point
- numeric definite integral
"""

import math


SAFE_GLOBALS = {
    name: getattr(math, name)
    for name in dir(math)
    if not name.startswith("_")
}
SAFE_GLOBALS["abs"] = abs


def f(expr: str, x: float) -> float:
    scope = {**SAFE_GLOBALS, "x": x}
    return float(eval(expr, {"__builtins__": {}}, scope))


def derivative(expr: str, x: float, h: float = 1e-5) -> float:
    return (f(expr, x + h) - f(expr, x - h)) / (2 * h)


def integral(expr: str, a: float, b: float, n: int = 1000) -> float:
    if n % 2 != 0:
        n += 1
    h = (b - a) / n
    total = f(expr, a) + f(expr, b)
    for i in range(1, n):
        coeff = 4 if i % 2 else 2
        total += coeff * f(expr, a + i * h)
    return total * h / 3


def main() -> None:
    print("Calculus Calculator")
    print("Use Python-style expression, e.g. x**2 + sin(x)")
    print("1) Evaluate f(x)")
    print("2) Derivative f'(x) at x")
    print("3) Definite integral from a to b")

    choice = input("Choose 1-3: ").strip()
    expr = input("f(x) = ").strip()

    try:
        if choice == "1":
            x = float(input("x = ").strip())
            print("Result:", f(expr, x))
        elif choice == "2":
            x = float(input("x = ").strip())
            print("Result:", derivative(expr, x))
        elif choice == "3":
            a = float(input("a = ").strip())
            b = float(input("b = ").strip())
            print("Result:", integral(expr, a, b))
        else:
            print("Invalid choice.")
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
