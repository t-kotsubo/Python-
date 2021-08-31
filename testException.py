class TestException(Exception):
    pass

def test(num: int):

    try:
        if type(num) != int:
            raise TestException(f"テストエラー: {num}")

    except TestException as e:
        print(f"e:{e}")
        print("型エラーが発生しました。")

    except Exception as e:
        print(f"e:{e}")
        print("通常エラーが発生しました。")        
