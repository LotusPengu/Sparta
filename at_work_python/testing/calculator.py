def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def divide(num1, num2):
    if num2 == 0:
        print("Please number MUST NOT BE DIVIDED BY ZERO!")
        raise ValueError("Cannot divide by zero")
    return num1 / num2
