from os import rmdir, mkdir, listdir
from os.path import join, isdir, isfile


def print_directory_tree(folder_path):
    paths = [join(folder_path, content) for content in listdir(folder_path)]
    # files = [f for f in paths if isfile(f)]
    # dirs = [dir for dir in paths if isdir(dir)]
    [print(x) for x in paths]
    [print_directory_tree(dir) for dir in paths if isdir(dir)]

folder_path = 'file'
print_directory_tree(folder_path)
