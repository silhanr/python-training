import sys
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

total_score = sum(student_scores)

# print(total_score)
# print(max(student_scores))

maximum = -sys.maxsize - 1
for score in student_scores:
    print(maximum)
    if score > maximum:
        maximum = score

print(maximum)