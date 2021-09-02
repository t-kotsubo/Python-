name_list = [{"name": "taka", "age": 46, "address": "Yokohama", "nationality": "Japan"},
             {"name": "yoshi", "age": 46, "address": "Tokyo", "nationality": "UK"},
             {"name": "nori", "age": 46, "address": "Tokyo", "nationality": "USA"},
             ]

"""
 str.format()の引数に**とともに辞書を渡すと、その辞書からキーワードをキー
 にして取得した値に変換される。
"""

for name in name_list:
    message = "{name}は{age}歳です。{address}に住んでいます。"
    print(message.format(**name))
