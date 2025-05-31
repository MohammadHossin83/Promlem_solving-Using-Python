def check_pass(score):
    if score >= 10:
        return "قبول"
    else:
        return "مردود"

students = []

count = int(input("چند دانش‌آموز دارید؟ "))

for i in range(count):
    name = input("نام دانش‌آموز: ")
    score = float(input("نمره‌ی دانش‌آموز: "))
    students.append({"name": name, "score": score})

print("\n اطلاعات دانش‌آموزان:")
for student in students:
    print("نام:", student["name"])
    print("نمره:", student["score"])
    print("وضعیت:", check_pass(student["score"]))
    print("-" * 15)

scores = [s["score"] for s in students]

if len(scores) > 0:
    average = sum(scores) / len(scores)
    print("میانگین نمرات:", average)

    if average >= 10:
        print("کلاس در وضعیت خوبی است.")
    else:
        print("کلاس نیاز به تلاش بیشتر دارد.")
else:
    print("هیچ دانش‌آموزی وارد نشده است.")
