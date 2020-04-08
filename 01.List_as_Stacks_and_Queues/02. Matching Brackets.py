def brackets_match(string):
    brackets = []
    for i in range(len(string)):
        if text[i] == "(":
            brackets.append(i)
        elif text[i] == ")":
            start_index = brackets.pop()
            print(text[start_index:i + 1])


text = input()
brackets_match(text)


# Input
# 1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5

# Output
# (2 + 3)
# (3 + 1)
# (2 - (2 + 3) * 4 / (3 + 1))