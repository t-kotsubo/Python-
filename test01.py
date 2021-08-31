list = [3, 4, 6]

for i, v in enumerate(list):
    if v % 2 == 1:
        break
else:
    print('奇数を代入してください')