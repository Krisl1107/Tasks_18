import json
import functools


def form_json(func):
    """
    A decorator that converts a function's return value to a JSON string.

    This decorator takes the result of the decorated function and serializes it
    into a formatted JSON string with proper UTF-8 encoding and indentation.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: A wrapper function that returns a JSON string.
    """
    def wrapper(*args, **kwargs):
        """
        Wrapper function that executes the original function and converts the result to JSON.

        Args:
            *args: Variable positional arguments passed to the original function.
            **kwargs: Variable keyword arguments passed to the original function.

        Returns:
            str: A JSON string representation of the function's return value.
        """
        result = func(*args, **kwargs)
        return json.dumps(result, ensure_ascii=False, indent=2)
    return wrapper

@form_json
def sportsmen_data():
    return  {
        "name": "Кристина",
        "age": 19,
        "city": ["Благовещенск", "Новосибирск"],
        "sport": "плавание",
        "sport category": "КМС"

    }

@form_json
def lst_numbers(num_1,num_2):
    return [num * 2 for num in range(num_1, num_2)]


@form_json
def get_user_data():
    return {
        "users_1": [
            {"id": 21937, "name": "Семём"},
            {"id": 17263, "name": "Аркадий"}
        ],
        "add_id":
            { "id_1": 26337,
             "id_2": 17373 }

           }
print(sportsmen_data())
print(lst_numbers(2, 30))
print(get_user_data())
