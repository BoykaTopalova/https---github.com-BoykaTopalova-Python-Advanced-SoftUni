number = int(input())
elements = set()
for i in range(number):
    x = [x for x in input().split()]
    for j in x:
        elements.add(j)
[print(k) for k in elements]
