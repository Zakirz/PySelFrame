from Core.App import App
from PageFactory.HomePage.HomePage import HomePage


class Test_Homepage(App):

    # def tests(self):
    #     try:
    #         self.homepage = HomePage()

    #         self.test_instantiate()
    #     except Exception as err:
    #         self.logger.critical(f"{err.__class__.__name__} {err} {err.__traceback__.tb_lineno}")

    def test_instantiate(self):
        self.navigate_to_url(self.BASE_URL)