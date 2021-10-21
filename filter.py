x = (3, 9, 4, 7, 0, 10)

ans1 = filter(lambda x: x % 3 == 0, x)
print(list(ans1))

# 第一引数にNoneを渡すと真になるオブジェクトだけが残る
ans2 = filter(None, x)
print(list(ans2))
