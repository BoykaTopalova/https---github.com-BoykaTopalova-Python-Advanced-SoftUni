def age_assignment(*args, **kwargs):
    result = {}
    for person in args:
        result[person] = kwargs[person[0]]

    return result


print(age_assignment("Peter", "George", G=26, P=19))
