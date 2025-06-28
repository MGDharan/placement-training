# Filename:  greatest_common_divisor.py
def gcd(a, b):
    while(b):
        a, b = b, a % b
    return a