def get_book_upper(index):
    items = ["note", "notebook", "sketchbook"]

    try:
        book = items[index]
    except (IndexError, TypeError) as e:
        print(f"例外が発生しました。: {e}")
    else:
        print(book)
    finally:
        print("終了します。")
get_book_upper(2)



