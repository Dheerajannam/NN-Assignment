class_score = float(input("Enter the class score: "))


if 90 <= class_score <= 100:
    grade = "A"
elif 80 <= class_score < 90:
    grade = "B"
elif 70 <= class_score < 80:
    grade = "C"
else:
    grade = "Below C"

print(f"Letter Grade: {grade}")
