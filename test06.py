from testException import TestException


class TestBaseException(Exception):
    """ ベースとなる例外クラス """

class TestPracticeException1(TestBaseException):
    """ ベースとなる例外クラス """

    def response_message1(self, error:str):
        print({"エラー内容": {error}})

class TestPracticeException2(TestBaseException):
    """ ベースとなる例外クラス """

    def response_message2(self, error:str):
        print({"エラー内容": {error}})

def TestException(num:int):
    try: 
        if type(num) != int:
            raise TestPracticeException1("Test1です。")

        if num >= 100:
            raise TestPracticeException2("Test2です。")

    except TestPracticeException1 as e:
            error = TestPracticeException1()
            error.response_message1(e)
            
    except TestPracticeException2 as e:
            error = TestPracticeException2()
            error.response_message2(e)

TestException("1000")