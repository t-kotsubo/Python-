from concurrent import futures
from concurrent.futures import (ThreadPoolExecutor, Future)
from time import sleep


def func():
    """ 非同期に行いたい処理 """
    sleep(60)
    return 1


# 非同期に行いたい処理をsubmit()に渡す
# ThereadPoolExecutorはExecutorの具象サブクラス
# 呼び出し可能オブジェクトをsubmit()に渡すと、その実行が
# スケジューリングされてFutureクラスのインスタンスが返される
# 処理の実行後、メソッドfuture.result()で呼び出し可能オブジェクト
# からの戻り値を取得できる
future = ThreadPoolExecutor().submit(func)
print(future)
# print(type(future)
# print(isinstance(future, Future))


print(future.result())
print(future.done())

# print(future.running())
# print(future.cancelled())
