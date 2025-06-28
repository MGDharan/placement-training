# Filename:  palindrome_checker.py
def is_palindrome(text):
    processed_text = ''.join(c for c in text.lower() if c.isalnum())
    return processed_text == processed_text[::-1]