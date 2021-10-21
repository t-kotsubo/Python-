def display_data(name, age, address):
    print(f"I am {name}, I am {age}years old, I live in {address}.")


# リストやタプルのアンパック(*を使用)
data_list = ['taka', 46, "Yokohama"]
display_data(*data_list)

# 辞書のアンパック(**を使用)
data_dict = {"name": "Kotsubo", "age": 46, "address": "Yokohama"}
display_data(**data_dict)
