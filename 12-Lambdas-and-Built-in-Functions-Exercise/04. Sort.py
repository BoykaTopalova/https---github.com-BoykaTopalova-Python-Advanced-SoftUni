numbers = list(map(int, input().split(" ")))
negative_numbers = filter(lambda x: x < 0, numbers)
sum_negative_numbers = sum(negative_numbers)
print(abs(sum_negative_numbers))
