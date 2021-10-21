class Threshold:
    def __init__(self, threshold):
        self.threshold = threshold

    # 特殊メソッド__call__()を持つインスタンスは()をつけて呼び出せる。
    def __call__(self, x):
        return self.threshold < x
    pass


# インスタンス化時にしきい値を指定
threshold = Threshold(2)

# __call__()が呼ばれる
print(threshold(3))

print(callable(threshold))
