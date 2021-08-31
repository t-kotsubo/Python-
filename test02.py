booklist = ["letter", "camera", "note"]


while booklist:
item = booklist.pop()
    if 'book' in item:
        print('Found!')
        break
else:
    print('Not Found!')
