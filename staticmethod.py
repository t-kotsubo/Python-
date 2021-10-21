class Page:
    def __init__(self, num, content):
        self.num = num
        self.content = content

    @staticmethod
    def check_blank(page):
        """
        スタティックメソッドの引数にはインスタンスやクラスオブジェクトは
        渡されず、呼び出し時に渡した値がそのまま渡される。つまり、スタティック
        メソッドはただの関数と同じ
        """
        return bool(page.content)


page1 = Page(1, '')
page2 = Page(2, 'test')

print(page1.check_blank(page1))
print(page2.check_blank(page2))
