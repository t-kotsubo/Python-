listA = ["one", "two", "three", "four", "five"]
filtered = list(filter(lambda x: len(x) >= 4, listA))
print(filtered)
