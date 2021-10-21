from dataclasses import dataclass
from functools import lru_cache
from time import sleep


# 最近の呼び出し最大32回分までキャッシュ
@lru_cache(maxsize=32)
def heavy_function(n):
    sleep(3)
    return n + 1


# 初回は時間が掛かる
print(heavy_function(3))
# キャッシュにヒットするのですぐに結果を得られる
print(heavy_function(3))


@dataclass(frozen=True)
class Fruit:
    name: str
    price: int = 0


apple = Fruit(name='apple', price=128)
print(apple)

# frozen=Trueとしたので読み取り専用：値を更新しようとするとエラー
apple.price = 256
