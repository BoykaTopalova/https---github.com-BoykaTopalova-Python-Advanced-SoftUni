vip = []
normal = []
yes = " "

while True:
    numbers = input()
    if numbers[0].isdigit():
        vip.append(numbers)
    elif numbers[0].isalpha() and numbers != "PARTY":
        normal.append(numbers)
    if numbers == "PARTY":
        break
while True:
    yes = input()
    if yes in normal:
        normal.remove(yes)
    if yes in vip:
        vip.remove(yes)

    if yes == "END":
        break

print(len(vip)+len(normal))
for item in vip:
    print(item)
for it in normal:
    print(it)
