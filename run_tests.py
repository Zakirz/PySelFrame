# from Core.BrowserHelpers import BrowserHelpers
import click
import os
import pytest

from Core.App import App


class RunUITests(App):
    def __init__(self):
        try:
            self.start_execution()
            pytest.main([f"--rootdir={self.BASE_DIR}/pytest_configs", "-s", "-v", f"{os.getcwd()}\\UI_Tests\\UI_Cases.py",
                         "--html=" + self.HTML_REPORT_FILE,
                         "--junit-xml=" + self.XML_REPORT_FILE,
                         "--self-contained-html",
                         "--maxfail", self.MAX_FAIL,
                         ])
        finally:
            self.stop_execution()


class RunAPITests(App):
    def __init__(self):
        pytest.main([f"--rootdir={self.BASE_DIR}/pytest_configs", "-s", "-v", f"{os.getcwd()}\\API_Tests\\API_Cases.py",
                      "--html=" + self.HTML_REPORT_FILE,
                      "--junit-xml=" + self.XML_REPORT_FILE,
                      "--self-contained-html",
                      "--maxfail", self.MAX_FAIL,
                      ])


@click.command()
@click.option('-m', default=None, help='Options run: debug')
def run(m):
    if m is None or m == "run":
        RunUITests()
    elif m == "api":
        RunAPITests()

#     @click.command()
#     @click.option('-m', default=None, help='Options run: debug')
#     def run(self, m):
#         if m is None or m == "run":
#             try:
#                 self.start_execution()
#                 pytest.main([f"--rootdir={self.BASE_DIR}/pytest_configs", "-s", "-v", f"{os.getcwd()}\\UI_Tests\\Cases.py",
#                               "--html=" + self.HTML_REPORT_FILE,
#                               "--junit-xml=" + self.XML_REPORT_FILE,
#                               "--self-contained-html",
#                               "--maxfail", self.MAX_FAIL,
#                               ])
#             finally:
#                 self.stop_execution()
#         elif m == "debug":
#             print("Debug Mode")
#             pytest.main(["-v", "-s", f"{os.getcwd()}\\UI_Tests\\Cases.py"])
#             print("Finished Debug Mode")


if __name__ == '__main__':
    run()
