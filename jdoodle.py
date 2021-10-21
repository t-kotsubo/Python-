book_list = ['notebook', 'text', 'sketchbook']


# for item in book_list:
#     if not 'book' in item:
#         continue
#     print(item)
# else:
#     print("終了しました。")

def has_book(items):

    copied = items.copy()

    while copied:
        item = copied.pop()

        if not 'book' in item:
            continue

        print(item)
    else:
        print("終了しました。")


has_book(book_list)
