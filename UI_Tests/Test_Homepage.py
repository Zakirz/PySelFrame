from Core.App import App


class Test_Homepage(App):

    def test_first(self):
        self.navigate_to_url(self.BASE_URL)
        self.get_text("Product Nav#xpath=//a[text()='Product']")
