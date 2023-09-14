# This code is supposed to calculate the factorial of a given integer. (4!)
# However, it has some issues that need to be fixed.

def calculate_factorial(n):
    result = 0

    for i in range(n):
        result *= i

    return result


# Example usage:
n = 5
result = calculate_factorial(n)
print(f"The factorial of {n} is {result}")


