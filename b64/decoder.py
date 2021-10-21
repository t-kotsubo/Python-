import base64
import sys
from typing import overload
import typing_extensions


def base64_to_str(x):
    """文字列をbase64表現に変換する
       b64encode()はbytes-like objectを引数に取るため
       文字列はencode()でbytes型にして渡す
    """
    return base64.b64decode(x).decode('utf-8')


if __name__ == '__main__':
    target = sys.argv[1]
    print(base64_to_str(target))


def test():
    print("hello")


__all__ = ['base64_to_str']
