set_a = {'note', 'notebook', 'sketchbook'}
set_b = {'book', 'rulebook', 'sketchbook'}

print("和集合")
# 和集合
print(set_a | set_b)
# 和集合はset.union()でも同様に求められる
print(set_a.union(set_b))


print("差集合")
# 差集合
print(set_a - set_b)
# set.difference()でも同様に求められる
print(set_a.difference(set_b))

print("積集合")
# 積集合
print(set_a & set_b)
# set.intersection()でも同様に求められる
print(set_a.intersection(set_b))

print("対称差")
print(set_a ^ set_b)
# set.symmetric_difference()でも同様に求められる
print(set_a.symmetric_difference(set_b))

print("部分集合か判定")
print({'note', 'notebook'} <= set_a)
# set.issubset()でも同様に求められる
print({'note', 'notebook'})
