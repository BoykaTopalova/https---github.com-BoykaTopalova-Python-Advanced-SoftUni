from random import choice, shuffle
from random import shuffle as randomise
import random
import random as my_random

fruits = ['apple', 'orange', 'banana', 'apricot', 'watermelon']
print(choice(fruits))
print(choice(fruits))
print(fruits)
random.shuffle(fruits)
print(fruits)
my_random.shuffle(fruits)
print(fruits)
randomise(fruits)
print(fruits)