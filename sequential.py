import time
from urllib import request
from pathlib import Path
# pythonでハッシュ化するにはhashlibを使う
from hashlib import md5
print('before urls')
urls = [
    'https://twitter.com',
    'https://facebook.com',
    'https://instagram.com',
]


def download(url):
    req = request.Request(url)
    # ファイル名に/などが含まれないようにする
    # halib.md5の引数に文字列を渡してencodeを行う
    # hexdigestで16進数文字列に変換する
    name = md5(url.encode('utf-8')).hexdigest()
    file_path = './' + name
    print(f"{file_path=}")
    with request.urlopen(req) as res:
        Path(file_path).write_bytes(res.read())
        return url, file_path


# 動きを確認
# download(urls[0])


def elapsed_time(f):
    def wrapper(*args, **kwargs):
        st = time.time()
        v = f(*args, **kwargs)
        print(f"{f.__name__}: {time.time() - st}")
        return v
    return wrapper


@elapsed_time
def get_sequential():
    for url in urls:
        print(f"downloaed_url{download(url)}")


get_sequential()
