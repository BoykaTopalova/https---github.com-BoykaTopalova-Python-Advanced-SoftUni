def args_length(*args):
    count = 0
    for _ in args:
        count += 1
    return count


print(args_length(1, 32, 5))
