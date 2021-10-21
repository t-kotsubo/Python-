from contextlib import contextmanager


@contextmanager
def test_contextManager(*args, **kwargs):
    return_list = []
    try:
        print("__enter__() was called.")
        if args:
            return_list.append(args)

        if kwargs:
            return_list.append(kwargs)

        yield return_list
    except Exception as e:
        print(e)
        raise

    finally:
        print("__exit__() was called.")


with test_contextManager(10, name="Takayuki") as c:
    print(c)
