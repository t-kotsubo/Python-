lst_a = ["4", 1, "7", 3]
lst_b = ["8", 4, "5", 2]

lst_a.sort(key=lambda x: int(x), reverse=True)
print(lst_a)
