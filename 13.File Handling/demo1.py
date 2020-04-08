file_path = "demo9.py"
try:
    file = open(file_path, 'r')
except FileNotFoundError:
    print('File not found')

