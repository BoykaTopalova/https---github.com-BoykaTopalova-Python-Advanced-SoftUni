list_char = input().split(", ")
occurrences = {word: ord(word) for word in list_char}
print(occurrences)