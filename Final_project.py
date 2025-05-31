def check_pass(score):
    if score >= 10:
        return "قبول"
    else:
        return "مردود"

students = []

students.append({"name": "ali", "score": 17})
students.append({"name": "mohammad", "score": 8})
students.append({"name": "reza", "score": 14})

students.remove({"name": "mohammad", "score": 8})

for student in students:
    print("نام:", student["name"])
    print("نمره:", student["score"])
    print("وضعیت:", check_pass(student["score"]))
    print("-" * 15)

scores = [s["score"] for s in students]
average = sum(scores) / len(scores)
print("میانگین نمرات:", average)

if average >= 10:
    print("کلاس در وضعیت خوبی است.")
else:
    print("کلاس نیاز به تلاش بیشتر دارد.")
