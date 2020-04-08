from termcolor import colored
from pyfiglet import figlet_format

print(colored('It works', 'red'))

text = colored('Hello World!', 'green', 'on_grey', attrs=['bold', 'underline'])
print(text)
# text = figlet_format("Python", font="isometric1")
text = colored(figlet_format("Python", font="isometric1"), 'blue', 'on_red', attrs=['bold'])
print(text)
