def sum_multiples(num_1: int, num_2: int, div_1: int, div_2: int) -> int:
    """
    Calculates the sum of natural numbers in the interval [num_1; num_2]
    that are multiples of div_1 and div_2.

    Parameters:
        num_1 (int): start of interval (inclusive)
        num_2 (int): end of interval (inclusive)
        div_1 (int): first multiple
        div_2 (int): second multiple

    Returns:
        int: sum of numbers meeting the condition
    """
    numbers = [num for num in range(num_1, num_2 + 1)]

    multiples = list(filter(lambda x: x % div_1 == 0 and x % div_2 == 0, numbers))

    return sum(multiples)


num_1 = int(input("Enter the start of the interval: "))
num_2 = int(input("Enter the end of the interval: "))
div_1 = int(input("Enter the first divisor: "))
div_2 = int(input("Enter the second divisor: "))

print("Sum of multiples:", sum_multiples(num_1, num_2, div_1, div_2))
