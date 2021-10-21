from urllib.request import urlopen

with urlopen('https://www.yahoo.co.jp') as u:
    print(u.info())
    print(u.read())
