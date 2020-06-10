import sys
import math


def read_coefficient(coefficient_name):
    try:
        return float(input("Enter a real number for the " + coefficient_name + " coefficient: "))
    except ValueError:
        print("You entered an invalid number")
        sys.exit(1)


a = read_coefficient("a")

if a == 0:
    print("The a coefficient cannot be equal to zero")
    sys.exit(1)

b = read_coefficient("b")
c = read_coefficient("c")

print("Standard form: f(x) =", "{:+.4f}".format(a), "x^2", "{:+.4f}".format(b), "x", "{:+.4f}".format(c))

# TODO: check if a not 0
# TODO: space clean up in the functional form

delta = b ** 2 - 4 * a * c
p = -b / (2 * a)
q = -delta / (4 * a)

# TODO: do not duplicate r1 and p

print("Vertex form: f(x) =", "{:+.4f}".format(a), "(x", "{:+.4f}".format(p), ")^2", "{:+.4f}".format(q))

if delta >= 0:
    roots = []
    if delta > 0:
        r1 = (-b - math.sqrt(delta)) / (2 * a)
        r2 = (-b + math.sqrt(delta)) / (2 * a)
        print("Factored form: f(x) =", "{:+.4f}".format(a), "(x", "{:+.4f}".format(r1), ")(x", "{:+.4f}".format(r2), ")")
        print("Roots of this quadratic function are:", "{:+.4f}".format(r1), "and", "{:+.4f}".format(r2))
    else:
        r1 = -b / (2 * a)
        print("Factored form: f(x) =", "{:+.4f}".format(a), "(x", "{:+.4f}".format(r1), ")^2")
        print("The only root of this quadratic function is:", "{:+.4f}".format(r1))
else:
    print("This quadratic function has no roots")
