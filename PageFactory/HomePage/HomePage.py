from Core.BrowserHelpers import BrowserHelpers
from . import homepage_or


class HomePage(BrowserHelpers):
    def __init__(self):
        self.obj = homepage_or
        super().__init__()

    def assert_recent_winners(self, input_string):
        return self.get_text(self.obj.recent_winners_link)


# https://statsroyale.com/
