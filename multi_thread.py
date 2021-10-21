from hashlib import md5
from pathlib import Path
from urllib import request

# マルチスレッドで平行化
from concurrent.futures import(
    ThreadPoolExecutor,
    as_completed
)
import time

from sequential import download

urls = [
    'https://twitter.com'
    'https://facebook.com'
    'https://instagram.com'
]


def elapsed_time(f):
    def wrapper(*args, **kwargs):
        st = time.time()
        v = f(*args, **kwargs)
        print(f"{f.__name__}: {time.time() - st}")
        return v
    return wrapper


@elapsed_time
def get_multi_thrad():
    """
        max_workersのデフォルトはコア数×5
        ThreadPoolExecutorクラスのインスタンスはコンテキストマネージャーになっているのでwith文で利用可能
        * 非同期実行する処理をメソッドexecutor.submit()で登録する
          (※もし呼び出し時に渡したいパラメータがある場合は第2引数以降に指定)
        * 非同期処理の実行結果はexcuter.submit()の戻り値のメソッドresult()を呼び出すと取得可能
        * as_completed()関数は、処理が完了したものから順番に返してくれる
    """

    with ThreadPoolExecutor(max_workers=3) as executor:  # 　引数：max_workersで最大スレッド数を指定
        futures = [executor.submit(download, url) for url in urls]

    for future in as_completed(futures):
        # 完了したものから取得できる
        print(future.result())
