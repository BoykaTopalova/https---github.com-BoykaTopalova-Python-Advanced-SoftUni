n = int(input())
matrix = [[int(i) for i in input().split(", ")] for j in range(n)]

first_diagonal = [matrix[i][i] for i in range(n)]
second_diagonal = [matrix[i][n - 1 - i] for i in range(n)]
sum_first = sum(first_diagonal)
sum_second = sum(second_diagonal)
print(f"First diagonal: {', '.join([str(x) for x in first_diagonal])}. Sum: {sum_first}")
print(f"Second diagonal: {', '.join([str(x) for x in second_diagonal])}. Sum: {sum_second}")
