file_path = 'file\\text1.txt'
try:
    file = open(file_path, 'r')
    print('File found')
except FileNotFoundError as e:
    print(e)
    print('File not found')
except:
    print('Unknown exception')
finally:
    print('End')
