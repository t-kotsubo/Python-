book = "Pyton実践入門"
# UTF-8を指定してエンコード
encoded = book.encode("utf-8")
print(f"type(encoded): {type(encoded)}")
print(encoded)

decoded = encoded.decode('utf-8')
print(f"decoded: {decoded}")
