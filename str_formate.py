class Test:
    """ testクラス """

    def __init__(self, name):
        self.name = name

    # def __str__(self):
    #     return "testクラスです"

    def test_method(self):
        """ test_mothodです """
        pass


print(Test.__doc__)

c_t = Test("taka")

print(isinstance(c_t, Test))

# __doc__を付けるとdocstringの内容がprintで表示される
print(f"test_method:{Test.test_method.__doc__}")
# print(dir(dct))

# print(f"{firstname=}: {familyname=}")
# name = ("Takayuki."
# "Kotsubo")

# print(name)

print("{0}の名前は{1}です。".format("俺", "崇行"))

print("姓：{familyname}、名前{firstname}".format(
    familyname="Kotsubo", firstname="Takayuki"))


# d = {'X': 'note', 'y':'notebook', 'z':'sketchbook'}
# books = "X: {X} z: {z}"

# print(books.format(**d))

# 重要 formateは辞書を使う組み合わせで便利
Takayuki = {"age": 46, "profession": "engineer", "address": "Yokohama"}

print("My age is {age}, I am workings as a {profession}. I live in {address}.".format(
    **Takayuki))
