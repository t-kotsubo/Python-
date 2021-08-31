# firstname = "Takayuki"
# familyname = "Kotsubo"

# print(f"{firstname=}: {familyname=}")
# name = ("Takayuki."
# "Kotsubo")

# print(name)

print("{0}の名前は{1}です。".format("俺", "崇行"))

print("姓：{familyname}、名前{firstname}".format(familyname="Kotsubo", firstname="Takayuki"))


# d = {'X': 'note', 'y':'notebook', 'z':'sketchbook'}
# books = "X: {X} z: {z}"

# print(books.format(**d))

Takayuki = { "age": 46, "profession":"engineer", "address": "Yokohama"}

print("My age is {age}, I am workings as a {profession}. I live in {address}.".format(**Takayuki))


