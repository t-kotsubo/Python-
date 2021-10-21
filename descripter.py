class TestField:
    """ __set__()を持つクラスはデータディスクリプタ """

    def __set_name__(self, owner, name):
        print('__set_name__ was called')
        print(f'{owner=}, {name=}')
        self.name = name

    def __set__(self, instance, value):
        print('__set__ was called')
        if not isinstance(value, str):
            raise AttributeError(f'{value} must be str ')
        # ドット記法ではなく属性辞書を使って格納
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        print('__get__ was called')
        return instance.__dict__[self.name]


class Book:
    title = TestField()


book = Book()
# 代入時には__set__()が呼ばれる
book.title = 'Python Practice Book'
print(f"{type(book.title)=}")


# 取得時には__get__()が呼ばれる
print(book.title)

# 別のインスタンスを作成して代入
notebook = Book()
notebook.title = 'Notebook'

# それぞれデータを保持している
print(book.title)
print(notebook.title)


class TextField:
    """ __get__()のみであれば非データデスクリプタ """

    def __init__(self, value):
        if not isinstance(value, str):
            raise AttributeError(f'{value} must be str')

        self.value = value

    def __set_name__(self, owner, name):
        print('__set_name__ was called')
        print(f'{owner=}, {name=}')
        self.name = name

    def __get__(self, instance, owner):
        print('__get__ was called')
        return self.value


class Book:
    title = TextField("Python Practice Book")


b = Book()
print(f'{b.title=}')
print(f'{type(b)=}')
print(type(b.title))
