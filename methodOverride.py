class Page:
    def __init__(self, num, content):
        self.num = num
        self.content = content

    def output(self):
        return f"{self.content}"


class TitlePage(Page):
    def output(self):
        title = super().output()
        return title.upper()


if __name__ == 'main':
    page = TitlePage(1, "test")
    print(page.output())
