def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a * 1.0 / b

def maximum(a, b):
    return a if a >= b else b


def minimum(a, b):
    return a if a <= b else b


print(add(3,4))
print(subtract(10,5))
print(multiply(5,5))
print(divide(10,5))
print(maximum(7,9))
print(minimum(5,1))