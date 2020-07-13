from Core.App import App


class Test_Homepage_2(App):

    def test_second(self):
        self.navigate_to_url(self.BASE_URL)
        self.get_text("Product Nav#xpath=//a[text()='Product']")
