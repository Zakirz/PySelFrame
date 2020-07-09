import re


class Locator():
    locator = None
    locator_type = None
    locator_description = None

    def parse_locator(self, enc_locator):
        try:
            pattern = r"^[a-zA-Z0-9_]*#([a-zA-Z_]+)=([\w\[\]()/@\'\":.+=#^$>*\-_])+$"
            if re.match(pattern, enc_locator):
                self.locator_description = enc_locator.split("#", 1)[0]
                self.locator_type, self.locator = enc_locator.split("#", 1)[
                    1].split("=", 1)
            else:
                self.locator_description = enc_locator.split("#", 1)[0]
                self.locator_type, self.locator = enc_locator.split("#", 1)[
                    1].split("=", 1)
            return self
        except re.error as err:
            print(err)
