import functools
from datetime import datetime


def exceptions(log_file="exceptions.log"):
    """
    A decorator that logs exceptions to a file.

    Args:
        log_file (str): Path to the log file. Defaults to "exceptions.log".

    Returns:
        function: Decorated function with exception logging.

    """

    def decor(func):
        def wrapper(*args, **kwargs):
            """
            Wrapper function that executes the original function and logs exceptions.

            Args:
                *args: Variable positional arguments passed to the original function.
                **kwargs: Variable keyword arguments passed to the original function.

            Returns:
                The result of the original function.

            Raises:
                Exception: Re-raises any exception caught during function execution.
            """
            try:
                return func(*args, **kwargs)
            except Exception as err:
                with open(log_file, "a", encoding="utf-8") as f:
                    f.write(f"[{datetime.now()}] {type(err).__name__}: {err}\n")
                raise

        return wrapper

    return decor


@exceptions("my_errors.log")
def divide(num_1, num_2):
    """
    Divides two numbers.

    Args:
        num_1 (int or float): The dividend (numerator).
        num_2 (int or float): The divisor (denominator).

    Returns:
        float: The result of num_1 divided by num_2.
    """
    return num_1 / num_2


if __name__ == "__main__":
    try:
        divide(200, 0)
    except ZeroDivisionError:
        print("ZeroDivisionError")

    try:
        divide(200, "4")
    except TypeError:
        print("TypeError")
