import sys
import math


def read_coefficient(coefficient_name):
    try:
        return float(input("Enter a real number for the " + coefficient_name + " coefficient: "))
    except ValueError:
        print("You entered an invalid number")
        sys.exit(1)


a = read_coefficient("a")
b = read_coefficient("b")
c = read_coefficient("c")

print("Standard form: f(x) =", a, "x^2 +", b, "x +", c)

# TODO: check if a not 0
# TODO: format - 4 decimal places
# TODO: minus signs in the functional form

delta = b ** 2 - 4 * a * c
p = -b / (2 * a)
q = -delta / (4 * a)

# TODO: do not duplicate r1 and p

print("Vertex form: f(x) =", a, "(x -", p, ")^2 +", q)

if delta >= 0:
    roots = []
    if delta > 0:
        r1 = (-b - math.sqrt(delta)) / (2 * a)
        r2 = (-b + math.sqrt(delta)) / (2 * a)
        print("Roots of this quadratic function are:", r1, "and", r2)
        print("Factored form: f(x) =", a, "(x -", r1, ")(x - ", r2, ")")
    else:
        r1 = -b / (2 * a)
        print("The only root of this quadratic function is:", r1)
else:
    print("This quadratic function has no roots")
