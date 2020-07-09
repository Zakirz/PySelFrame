from Core.App import App


class Test_Homepage(App):

    def test_title_stats_royale(self, start_log):
        start_log.info("in")
        pass

    def test_google(self, browser):
        browser.get("https://google.com/")
        assert browser.title
