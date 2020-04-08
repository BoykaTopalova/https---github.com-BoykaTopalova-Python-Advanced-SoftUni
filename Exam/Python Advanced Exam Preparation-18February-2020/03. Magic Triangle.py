def get_magic_triangle(n):
    first_list = [[1]]
    for i in range(1, n):
        temp_list = []
        for j in range(i + 1):
            if j == 0:
                temp_list.append(1)
            elif j == i:
                temp_list.append(1)
            else:
                temp_list.append(first_list[i - 1][j] + first_list[i - 1][j - 1])
        first_list.append(temp_list)
    return first_list


print(get_magic_triangle(5))
