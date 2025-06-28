# Filename:  list_comprehension_example.py
def square_even(numbers):
    return [x**2 for x in numbers if x % 2 == 0]