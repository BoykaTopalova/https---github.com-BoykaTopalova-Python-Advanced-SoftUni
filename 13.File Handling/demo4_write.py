file_path = 'file\\demo.txt'
result = [1, 2, 3, 4, 5, 6, 7]

with open(file_path, 'w') as file1:
    file1.write('Something else')
    file1.writelines(map(str, result))

# with open(file_path, 'w')as file2:
#     file2.write('Other thing')
#
# with open(file_path, 'w') as file1:
#     file1.write('Something else')
#     file1.writelines(map(str, result))