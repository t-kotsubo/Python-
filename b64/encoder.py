import base64
import sys


def str_to_base64(x):
    """文字列をbase64表現に変換する
       b64encode()はbytes-like objectを引数に取るため
       文字列はencode()でbytes型にして渡す
    """
    return base64.b64encode(x.encode('utf-8'))


if __name__ == '__main__':
    target = sys.argv[1]
    print(str_to_base64(target))

__all__ = ['str_to_base64']
