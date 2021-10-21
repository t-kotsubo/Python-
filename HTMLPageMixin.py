from methodOverride import Page


class HTMLPageMixin:
    def to_html(self):
        return f"<html><body>{self.output()}</body></html>"


class WebPage(Page, HTMLPageMixin):
    pass


page = WebPage(0, 'web content')
print(page.to_html())
