from math import sqrt
from functools import reduce

def squares_multiples(num_1: int, num_2: int, div: int) -> int:
    """
    Calculates the product of numbers in the interval [num_1; num_2]
    that are perfect squares and multiples of c.

    Parameters:
        num_1 (int): start of interval
        num_2 (int): end of interval
        div (int): divisor

    Returns:
        int: product of the numbers, or 1 if none found
    """

    numbers = [num for num in range(num_1, num_2 + 1)]

    filt_numbers = list(filter(
        lambda x: (sqrt(x).is_integer() and x % div == 0),
        numbers
    ))

    product = reduce(lambda x, y: x * y, filt_numbers, 1)

    return product


num_1 = int(input("Enter start of interval (a): "))
num_2 = int(input("Enter end of interval (b): "))
div = int(input("Enter divisor (c): "))

print(squares_multiples(num_1, num_2, div))
