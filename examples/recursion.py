def factorial_recursive(number):
    if number < 0:
        raise ValueError("number must be non-negative")
    if number <= 1:
        return 1
    return number * factorial_recursive(number - 1)

def factorial_iterative(number):
    if number < 0:
        raise ValueError("number must be non-negative")
    result = 1
    for value in range(2, number + 1):
        result *= value
    return result
