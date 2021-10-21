class Mutable:
    def __init__(self, attr_map):
        for k, v in attr_map.items():
            setattr(self, str(k), v)


m = Mutable({'a': 1, 'b': 2, 'c': 3})

print(m.b)
print(getattr(m, 'b'))

delattr(m, 'c')
print(dir(m))
