def kwargs_length(**kwargs):
    length = 0
    for _ in kwargs:
        length += 1
    return length


dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))
