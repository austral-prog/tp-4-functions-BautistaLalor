# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    root1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    root2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
    determinante = b**2 - 4*a*c
    if root1 != root2 and determinante > 0:
        return f"({root1}, {root2})"
    elif root1 == root2 and determinante >= 0:
        return f"({root1})"
    else:
        return "( )"


def value_y(a, b, c, x):
    y = (a*x**2 + b*x + c)
    return y


def to_string(a, b, c):
    if a != 0 and b != 0 and c != 0:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"
    elif a == 0 and b != 0 and c != 0:
        return f"f(x) = {b} * X + {c}"
    elif a != 0 and b == 0 and c != 0:
        return f"f(x) = {a} * X^2 + {c}"
    elif a == 0 and b == 0:
        return f"f(x) = {c}"


def derivation(a, b, c):
    string = f"f'(x) = {2*a} * X + {b}"
    if a != 0 and b != 0:
        return f"f'(x) = {2*a} * X + {b}"
    elif a == 0 and b != 0:
        return f"f'(x) = {b}"
    elif a != 0 and b == 0:
        return f"f'(x) = {2*a} * X"
    else:
        return f"f'(x) = 0"
