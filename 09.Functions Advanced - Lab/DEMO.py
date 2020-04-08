def some_func(*args):
    print(args)


some_func(1, 2, 3)
some_func("peter", "george")
some_func(True, False)
some_func()
print("--------------------------------------")


def greet_me(**kwargs):
    for key, value in kwargs.items():
        print(f"{value}, {key}")


greet_me(Peter="Hello", George="Bye")

print("----------------------------------")


def print_nums(a, b, c):
    print(a, b, c)


nums = [1, 2, 3]
print_nums(*nums)
