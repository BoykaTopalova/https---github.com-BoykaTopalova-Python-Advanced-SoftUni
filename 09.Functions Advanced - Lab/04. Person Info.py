def get_info(name, town, age):
    text = f"This is {name} from {town} and he is {age} years old"
    return text


info = {"name": "George", "town": "Sofia", "age": 20}
print(get_info(**info))
