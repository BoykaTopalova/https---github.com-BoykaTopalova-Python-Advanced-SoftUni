file_path = "demo.py"

file = open(file_path, 'r')


# print(file.read(5))
# print(file.read(5))
# print(file.read(4))

while True:
    ch = file.read(1)
    if not ch:
        break
    print(ch, end='')