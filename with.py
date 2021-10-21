class ContextManager:
    """ with文に対応したオブジェクトをコンテキストマネージャーと呼ぶ """

    # 前処理を実装
    def __enter__(self):
        print(('__enter__ was called'))

    # 後処理を実行
    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__')
        print(f'{exc_type=}')
        print(f'{exc_value=}')
        print(f'{traceback=}')


# withブロックが正常終了の場合は__exit__()の引数はすべてNone
with ContextManager():
    print("inside the block")


# withブロック内で例外が発生した場合はその情報が__exit__()に渡される
with ContextManager():
    1/0
