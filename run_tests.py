# from Core.BrowserHelpers import BrowserHelpers
# import click
import os
import pytest

from Core.App import App


class RunTests(App):
    def __init__(self):
        try:
            self.start_execution()
            pytest.main([f"--rootdir={self.BASE_DIR}/pytest_configs", "-s", "-v", f"{os.getcwd()}\\Tests\\Cases.py",
                         "--html=" + self.HTML_REPORT_FILE,
                         "--junit-xml=" + self.XML_REPORT_FILE,
                         "--self-contained-html",
                         "--maxfail", self.MAX_FAIL,
                         ])
        finally:
            self.stop_execution()


def run():
    RunTests()

# @click.command()
# @click.option('-m', default=None, help='Options run: debug')
# def run(m):
#     if m is None or m == "run":
#         now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
#         init_env(now_time)
#         html_report = os.path.join(RunConfig.REPORT_DIR, now_time, "result.html")
#         xml_report = os.path.join(RunConfig.REPORT_DIR, now_time, "junit.xml")
#         pytest.main([f"--rootdir={RunConfig.BASE_DIR}/pytest_configs", "-s", "-v", f"{os.getcwd()}\\Tests\\Tests.py",
#                      "--html=" + html_report,
#                      "--junit-xml=" + xml_report,
#                      "--self-contained-html",
#                      "--maxfail", RunConfig.max_fail,
#                      ])
#     elif m == "debug":
#         print("Debug Mode")
#         pytest.main(["-v", "-s", f"{os.getcwd()}\\Tests"])
#         print("Finished Debug Mode")


if __name__ == '__main__':
    run()
