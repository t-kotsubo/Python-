from concurrent.futures import (ThreadPoolExecutor, wait)
import threading


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count = self.count + 1


class ThreadSafeCounter:
    # ロックを用意する
    lock = threading.Lock()

    def __init__(self):
        self.count = 0

    def increment(self):
        with self.lock:
            # 排他したい一連の処理をこのブロック内に書く
            self.count = self.count + 1


def count_up(counter):
    # 1,000,000回インクリメントする
    for _ in range(1_000_000):
        counter.increment()


# スレッドセーフでないカウンター
counter_unsafe = Counter()
# スレッドセーフなカウンター
counter_safe = ThreadSafeCounter()
threads = 2
with ThreadPoolExecutor() as e:
    # 2つのスレッドを用意にそれぞれでcount_upを呼び出す
    futures = [e.submit(count_up, counter_unsafe) for _ in range(threads)]
    done, not_done = wait(futures)

with ThreadPoolExecutor() as e:
    # 2つのスレッドを用意にそれぞれでcount_upを呼び出す
    futures = [e.submit(count_up, counter_safe) for _ in range(threads)]
    done, not_done = wait(futures)
# 数値をカンマ区切りで表示
print(f'{counter_unsafe.count=:,}')
print(f'{counter_safe.count=:,}')
