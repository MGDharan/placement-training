def calculate_polygon_area(sides, length):
    """Calculates the area of a regular polygon."""
    if sides < 3:
        raise ValueError("A polygon must have at least 3 sides.")
    
    apothem = length / (2 * tan(pi / sides))
    area = 0.5 * sides * length * apothem
    return area

from math import tan, pi


class EmailValidator:
    def __init__(self, allowed_domains):
        self.allowed_domains = allowed_domains

    def validate(self, email):
        try:
            username, domain = email.split('@')
            if domain not in self.allowed_domains:
                return False
            if not username:
                return False
            return True
        except ValueError:
            return False



def fibonacci_sequence(n):
    """Generates a Fibonacci sequence up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        list_fib = [0, 1]
        while len(list_fib) < n:
            next_fib = list_fib[-1] + list_fib[-2]
            list_fib.append(next_fib)
        return list_fib



class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance



def find_prime_factors(num):
    """Finds the prime factors of a given number."""
    i = 2
    factors = []
    while i * i <= num:
        while num % i == 0:
            factors.append(i)
            num //= i
        i += 1
    if num > 1:
        factors.append(num)
    return factors



class DataCleaner:
    def __init__(self, data):
        self.data = data

    def remove_duplicates(self):
        return list(set(self.data))

    def remove_nulls(self):
        return [x for x in self.data if x is not None]

    def to_lowercase(self):
        if all(isinstance(item, str) for item in self.data):
            return [x.lower() for x in self.data]
        return self.data



def count_word_frequency(text):
    """Counts the frequency of each word in a text."""
    words = text.lower().split()
    word_counts = {}
    for word in words:
        word = word.strip('.,!?"').lower()  # Remove punctuation and lowercase
        if word:  # Skip empty strings
            word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts



class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


def is_palindrome(text):
  processed_text = ''.join(filter(str.isalnum, text)).lower()
  return processed_text == processed_text[::-1]