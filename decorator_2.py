# デコレートしたい関数を受け取る
def decol(f):
    print('decol called')

    def wrapper():
        """ プログラムの実行中にもとの関数が呼び出されると
        もとの関数の代わりにwrapper()関数が実行される。"""

        print('before exec')
        v = f()  # 　もとの関数を実行
        print('after exec')
        return v
    return wrapper


def deco2(f):
    print('deco2 called')

    # 引数を受け取り実行する
    def wrapper(*args, **kwargs):
        print('before exec')
        v = f(*args, **kwargs)  # 　もとの関数を実行
        print('after exec')
        return v
    return wrapper


@decol
def func1():
    print('exec')
    return 1


@deco2
def func2(x, y):
    print('exec')
    return x + y


result1 = func1()
print(f'result1: {result1}')

result2 = func2(3, 5)
print(f'result2: {result2}')


def deco3(z):
    # deco2と同様
    print('start deco3')

    def _doce3(f):
        def wapper(*args, **kwargs):
            # ここでzを参照できる
            print('before exec', z)
            v = f(*args, **kwargs)
            print('after exec', z)
            return v
        return wapper
    return _doce3  # デコレータを返す


@deco3(z=3)
def func3(x, y):
    print('exec')
    return x, y


result3 = func3(1, 3)
print(f"result3: {result3}")


@deco3(z=3)
@deco3(z=4)
def func4(x, y):
    print('exec')
    return x, y


result4 = func4(1, 2)
print(f'result4: {result4}')
