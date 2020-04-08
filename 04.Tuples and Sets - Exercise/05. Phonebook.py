phonebook = {}
while True:
    elements = input()
    if elements == "search":
        break
    elem = elements.split("-")
    name = elem[0]
    phone = elem[1]
    phonebook[name] = phone
while True:
    search_name = input()
    if search_name == "stop":
        break
    if search_name in phonebook:
        print(f"{search_name} -> {phonebook[search_name]}")
    else:
        print(f"Contact {search_name} does not exist.")

    # for (name, phone) in sorted(phonebook.items(), key=lambda kvp: kvp[0], reverse=True):
    #
    #     if search_name == name:
    #         print(f"{search_name} -> {phone}")
    #         break
    #     elif search_name != name:
    #         print(f"Contact {search_name} does not exist.")
    #         break
