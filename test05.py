a, b, c = 0, -1, 0.01

# if a < b < c:
#     print("True")
# else:
#     print("False")

print(bool(a))
print(bool(b))
print(bool(c))

lstA = [1]
dictA = {"testA": 1}

print(bool(lstA))
print(bool(dictA))

if len(lstA) >= 0:
    print("True")

if lstA:
    print("True")
