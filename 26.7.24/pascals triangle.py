def print_pascals_triangle(n):
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = prev_row[j - 1] + prev_row[j]
        prev_row = row
        print(" ".join(map(str, row)))

# Input: number of rows
n = int(input("Enter the number of rows: "))

# Print Pascal's Triangle
print_pascals_triangle(n)
