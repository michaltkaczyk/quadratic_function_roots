import sys
import math
from sympy import Symbol, solve


def read_coefficient(coefficient_name):
    try:
        return float(input("Enter a real number for the " + coefficient_name + " coefficient: "))
    except ValueError:
        print("You entered an invalid number")
        sys.exit(1)


def format_coefficient(coefficient_value):
    return "{:+.4f}".format(coefficient_value).replace("+", "+ ").replace("-", "- ")


def show_roots_numeric(a, b, c):
    print("\nCalculating roots of a quadratic function using generic Python approach")
    print("Standard form: f(x) = ", format_coefficient(a), " x^2 ", format_coefficient(b),
          " x ", format_coefficient(c), sep="")

    delta = b ** 2 - 4 * a * c
    p = -b / (2 * a)
    q = -delta / (4 * a)

    print("Vertex form: f(x) = ", format_coefficient(a),
          " (x ", format_coefficient(-p), ")^2 ", format_coefficient(q), sep="")

    if delta >= 0:
        if delta > 0:
            r1 = (-b - math.sqrt(delta)) / (2 * a)
            r2 = (-b + math.sqrt(delta)) / (2 * a)
            print("Factored form: f(x) = ", format_coefficient(a),
                  " (x ", format_coefficient(-min(r1, r2)), ") (x ", format_coefficient(-max(r1, r2)), ")", sep="")
            print("Roots of this quadratic function are:",
                  "{:-.4f}".format(min(r1, r2)), "and", "{:-.4f}".format(max(r1, r2)))
        else:
            p = -b / (2 * a)
            print("Factored form: f(x) = ", format_coefficient(a), " (x ", format_coefficient(-p), ")^2", sep="")
            print("The only root of this quadratic function is:", "{:-.4f}".format(p))
    else:
        print("This quadratic function has no real roots")


def show_roots_symbolic(a, b, c):
    print("\nCalculating roots of a quadratic function using the SymPy library")

    x = Symbol("x")
    f = a * (x ** 2) + b * x + c
    roots = solve(f)

    is_root_real = list(map(lambda x: x.is_real, roots))
    real_roots = [root for (root, flag) in zip(roots, is_root_real) if flag]

    if len(real_roots) == 2:
        print("Roots of this quadratic function are:", real_roots[0], "and", real_roots[1])
    elif len(real_roots) == 1:
        print("The only root of this quadratic function is:", real_roots[0])
    else:
        print("This quadratic function has no real roots")


if __name__ == '__main__':
    a = read_coefficient("a")

    if a == 0:
        print("The a coefficient cannot be equal to zero")
        sys.exit(1)

    b = read_coefficient("b")
    c = read_coefficient("c")

    show_roots_numeric(a, b, c)
    show_roots_symbolic(a, b, c)
