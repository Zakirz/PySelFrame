# from Core.BrowserHelpers import BrowserHelpers
import click
import os
import pytest

from Core.App import App


class RunUITests(App):
    def __init__(self):
        try:
            pytest.main([
                f"--rootdir={self.BASE_DIR}/pytest_configs", "-s", f"{os.getcwd()}\\UI_Tests",
                "--html=" + self.HTML_REPORT_FILE,
                "--junit-xml=" + self.XML_REPORT_FILE,
                "--maxfail", self.MAX_FAIL,
            ])
        finally:
            self.stop_execution()


class RunAPITests(App):
    def __init__(self):
        pytest.main([
            f"--rootdir={self.BASE_DIR}/pytest_configs", "-s", "-v", f"{os.getcwd()}\\API_Tests",
            "--html=" + self.HTML_REPORT_FILE,
            "--junit-xml=" + self.XML_REPORT_FILE,
            "--self-contained-html",
            "--maxfail", self.MAX_FAIL,
        ])


@click.command()
@click.option('-m', default=None, help='Options run: debug')
def run(m):
    if m is None or m == "ui":
        RunUITests()
    elif m == "api":
        RunAPITests()


if __name__ == '__main__':
    run()
