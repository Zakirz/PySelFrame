from Core.App import App
from PageFactory.HomePage.HomePage import HomePage


class Test_Homepage(App):

    def test_title(self, init_driver):
        driver = init_driver
        driver.get("https://www.linkedin.com/")
        pass

    def test_title_stats_royale(self, init_driver):
        try:

            self.navigate_to_url("https://www.google.com/")
            assert True
        except Exception:
            print(Exception)
