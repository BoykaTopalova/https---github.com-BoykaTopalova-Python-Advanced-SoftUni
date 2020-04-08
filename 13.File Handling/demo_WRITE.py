file_path = 'file\\demo.txt'

file = open(file_path, 'w')
# file.write('Hello\n')
file.writelines('Hello')
file.writelines('World')