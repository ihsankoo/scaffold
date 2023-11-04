import math


def product(*args):
    return math.prod(args)


x = 2
y = 3
print(f"Product of {x} and {y} is {product(x, y)}")
