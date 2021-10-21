def f():
    x = "x"

    def g():
        nonlocal x  # nonlocal文 宣言
        x = 1
        print(x)

    g()
    print(x)


f()
