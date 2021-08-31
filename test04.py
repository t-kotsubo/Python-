class test:
    """ testクラス """

    def __init__(self, name):
        self.name = name

    # def __str__(self):
    #     return "testクラスです"

    def test_method(self):
        """ test_mothodです """
        pass

print(test.__doc__)

c_t = test("taka")

print(isinstance(c_t, test)

# dct = {}

# # print(isinstance(dct, dict))

# print(isinstance(dct, set))

# print(f"c_t:{c_t}")
# __doc__を付けるとdocstringの内容がprintで表示される
print(f"test_method:{test.test_method.__doc__}")
# print(dir(dct))
