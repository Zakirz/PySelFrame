from Core.App import App
from PageFactory.HomePage.HomePage import HomePage


class Test_Homepage(App):
    hompage = HomePage()

    def test_instantiate(self):
        self.navigate_to_url(self.BASE_URL)
        self.get_text("Product Nav#xpath=//a[text()='Product']")
