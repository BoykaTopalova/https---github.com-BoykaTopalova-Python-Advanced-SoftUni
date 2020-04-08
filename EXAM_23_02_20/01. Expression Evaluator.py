from collections import deque
from math import trunc

line_expression = deque(input().split(" "))
numbers_queue = deque()
result = 0
while line_expression:
    if line_expression[0].isnumeric():
        temp = line_expression.popleft()
        if int(temp) < 0:
            temp = abs(temp)
        numbers_queue.append(int(temp))
    else:
        sign = line_expression.popleft()
        while numbers_queue:
            if len(numbers_queue) == 1:
                break
            if sign == "*":
                result = numbers_queue.popleft() * numbers_queue.popleft()
                numbers_queue.appendleft(result)
            elif sign == "+":
                result = numbers_queue.popleft() + numbers_queue.popleft()
                numbers_queue.appendleft(result)
            elif sign == "-":
                result = numbers_queue.popleft() - numbers_queue.popleft()
                if result < 0:
                    result = abs(result)
                numbers_queue.appendleft(result)
            else:
                result = numbers_queue.popleft() / numbers_queue.popleft()
                result = trunc(result)
                numbers_queue.appendleft(result)

print(f"{result}")
