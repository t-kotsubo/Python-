from functools import wraps
import time


def deco4(func):
    @wraps(func)
    # デコレータを使う際は、標準ライブラリのデコレータ
    # functools.wraps()を使い、実際に実行される関数の名前やDocstringを
    # 元の関数のものに置き換えることが一般的
    def wrapper(*args, **kwargs):
        print('before exec')
        v = func(*args, **kwargs)
        print('after exec')
        return v
    return wrapper


@deco4
def tesfunc():
    """ testfuncです """
    print('exec')


print(tesfunc.__name__)
print(tesfunc.__doc__)


def elapsed_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        v = func(*args, **kwargs)
        print(f"{func.__name__}: {time.time() - start}")
        return v
    return wrapper


@elapsed_time
def testfunc2(n):
    return sum(i for i in range(n))


testfunc2(100)
