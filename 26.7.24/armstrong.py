def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    power = len(digits)
    return sum(d ** power for d in digits) == num

# Input: range start and end
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Find and print Armstrong numbers in the given range
print("Armstrong numbers within the given range:")
for num in range(start, end + 1):
    if is_armstrong(num):
        print(num)
