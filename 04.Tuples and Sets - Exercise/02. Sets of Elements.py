number = [int(x) for x in input().split()]
n = number[0]
m = number[1]
t1 = set()
t2 = set()
for i in range(n):
    num = input()
    t1.add(num)
for j in range(m):
    num1 = input()
    t2.add(num1)
for i in t1 & t2:
    print(i)
