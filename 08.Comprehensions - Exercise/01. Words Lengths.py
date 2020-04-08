# list_word = [word for word in input().split(", ")]
# dict_word = {word: len(word) for word in list_word}
# list_dict = [(f"{word} -> {length}") for (word, length) in dict_word.items()]
# print(", ".join(list_dict))

print(', '.join([f"{x} -> {len(x)}" for x in input().split(", ")]))