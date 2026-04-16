def count_numbers(num_1: int, num_2: int, div: int, last: int) -> int:
    """
    Counts the numbers in the interval [num_1; num_2] that are not divisible by div
    and end with the digit last.

    Parameters:
        num_1 (int): start of interval
        num_2 (int): end of interval
        div (int): divisor for the multiple check
        last (int): last digit the number should end with

    Returns:
        int: count of numbers satisfying the conditions
    """
    numbers = [num for num in range(num_1, num_2 + 1)]

    count_num = list(map(lambda x: (x % div != 0) and (x % 10 == last), numbers))

    return sum(count_num)


num_1 = int(input("Enter the start of the interval: "))
num_2 = int(input("Enter the end of the interval: "))
div_1 = int(input("Enter the first divisor: "))
last_num = int(input("Enter the last number: "))

print("Sum of numbers:", count_numbers(num_1, num_2, div_1, last_num))
