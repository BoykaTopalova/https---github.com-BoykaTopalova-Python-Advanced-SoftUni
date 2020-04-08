n = int(input())
students = {}


def average(gr):
    sums = 0
    for i in gr:
        sums += float(i)
    return sums / len(gr)


for i in range(n):
    line = input().split(" ")
    person = line[0]
    grade = float(line[1])
    if person not in students:
        students[person] = []
    students[person].append(f"{grade:.2f}")

for (name, grades) in students.items():
    print(f"{name} -> {' '.join(grades)} (avg: {average(grades):.2f})")
