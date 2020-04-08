file = open('file\\numbers.txt')
sums = 0
for line in file:
    sums += int(line)
print(sums)
