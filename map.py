x = (3, 9, 3, 7, 0, 10)

ans1 = map(lambda x: x * 2, x)
# 第一引数にNoneを渡すと真になるオブジェクトだけが残る
print(set(ans1))

keys = ('q', 'limit', 'page')
values = ('python', 10, 2)
# map()には、第二引数以降に複数のイテラブルを渡せる。
ans = map(lambda k, v: f"{k}={v}", keys, values)
print(list(ans))
