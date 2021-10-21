def gen_function(n):
    print('start')
    while n:
        print(f'yield: {n}')
        yield n
        n -= 1


# 戻り値はジェネレータイテレータ
gen = gen_function(2)
print(gen)

# 組み込み関数next()に渡すと
# __next__()が呼ばれる
print(next(gen))
print(gen)

print(next(gen))
print(gen)


# for文でジェネレーターを使用
# ジェネレーター関数とは内部でyield式を使っている関数のことをいう。
# ジェネレーター関数の戻り値がジェネレータイテレータと呼ばれるイテレータである。
# ジェネレーター関数は戻り値がイテレータのためfor文や内包表記、引数にイテラブルを取る関数などで利用が可能

def gen_function(n):
    n = 0
    while n <= 10:
        yield n
        n += 1


# for文でイテレータを使用
for i in gen_function(10):
    print(i)

# 内包表記でイテレータを使用
str_lst = [str(i) for i in gen_function(10)]
print(str_lst)

# イテラブルからジェネレータを作成する
gen_a = (i for i in range(10) if i % 2 == 0)
print(gen_a)
print(list(gen_a))
# メモ：ジェネレータは一度値を取り出されると無くなってしまう。
gen_b = (i for i in range(10) if i % 2 == 0)
print(tuple(gen_b))
