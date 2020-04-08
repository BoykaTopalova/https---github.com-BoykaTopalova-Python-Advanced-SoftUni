list_numbers = [int(num) for num in input().split(', ')]
positive = [str(n) for n in list_numbers if n >= 0]
negative = [str(n) for n in list_numbers if n < 0]
even = [str(n) for n in list_numbers if n % 2 == 0]
odd = [str(n)for n in list_numbers if n % 2 != 0]
print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")

