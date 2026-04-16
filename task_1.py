def upper_el(sent: str, index_1: int, index_2: int) -> int:
    """
    Counts the number of uppercase letters in a substring of the input string.

    Parameters:
        sent (str): The input string.
        index_1 (int): The starting index (1-based).
        index_2 (int): The ending index (1-based).

    Returns:
        int: The count of uppercase characters within the specified range.
    """
    upper_chars = list(filter(str.isupper, sent[index_1 - 1:index_2]))
    return len(upper_chars)


input_str = input("Enter a string: ")
index_1 = int(input("Enter the starting index: "))
index_2 = int(input("Enter the ending index: "))

print(upper_el(input_str, index_1, index_2))
