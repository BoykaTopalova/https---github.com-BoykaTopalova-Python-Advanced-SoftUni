numbers = list(map(int, input().split()))
negative_numbers = list(filter(lambda x: x < 0, numbers))
positive_numbers = list(filter(lambda x: x > 0, numbers))
sum_positive = sum(positive_numbers)
sum_negative = sum(negative_numbers)
print(sum_negative)
print(sum_positive)
if abs(sum_negative) > sum_positive:
    print(f"The negatives are stronger than the positives")
else:
    print(f"The positives are stronger than the negatives")
