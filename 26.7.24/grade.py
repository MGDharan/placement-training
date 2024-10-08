def calculate_average(total):
    return total / 5

def find_score(grade):
    if 90 <= grade <= 100:
        return "A"
    elif 80 <= grade <= 89:
        return "B"
    elif 70 <= grade <= 79:
        return "C"
    elif 60 <= grade <= 69:
        return "D"
    else:
        return "F"

scores = []
for i in range(1, 6):
    score = int(input(f"Enter score {i}: "))
    print("That's a(n): " + find_score(score))
    scores.append(score)

total = sum(scores)
avg_marks = calculate_average(total)
final_grade = find_score(avg_marks)

print(f"Average grade is: {avg_marks:.1f}")
print(f"That's a(n): {final_grade}")
output:
Enter score 1: 99
That's a(n): A
Enter score 2: 98
That's a(n): A
Enter score 3: 78
That's a(n): C
Enter score 4: 95
