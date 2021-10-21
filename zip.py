from itertools import zip_longest
lst_x = [1]
lst_y = ["a", "b", "c"]
lst_z = [True, False, True]

zip = zip(lst_y, lst_x, lst_z)
ziP_l = zip_longest(lst_x, lst_y, lst_z)
print(zip)
print(type(zip))

print(list(zip))
print(list(ziP_l))
