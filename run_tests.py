# from Core.BrowserHelpers import BrowserHelpers
from pytest_configs.conftest import REPORT_DIR, BASE_DIR
import click
import os
import time
import pytest
from Core.Configs import RunConfig


def init_env(now_time):
    CURRENT_REPORT_DIR = os.path.join(REPORT_DIR, now_time)
    if not os.path.exists(CURRENT_REPORT_DIR):
        os.mkdir(CURRENT_REPORT_DIR)
        os.mkdir(os.path.join(CURRENT_REPORT_DIR, "image"))


# class RunTests(BrowserHelpers):
#     def __init__(self):
#         try:
#             self.start_execution()
#         finally:
#             self.stop_execution()


@click.command()
@click.option('-m', default=None, help='Options run: debug')
def run(m):
    if m is None or m == "run":
        now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
        init_env(now_time)
        html_report = os.path.join(REPORT_DIR, now_time, "report.html")
        xml_report = os.path.join(REPORT_DIR, now_time, "junit-xml.xml")
        pytest.main([f"--rootdir={BASE_DIR}/pytest_configs", "-s", "-v", f"{os.getcwd()}\\Tests",
                     "--html=" + html_report,
                     "--junit-xml=" + xml_report,
                     "--self-contained-html",
                     "--maxfail", RunConfig.max_fail,
                     ])
    elif m == "debug":
        print("Debug Mode")
        pytest.main(["-v", "-s", f"{os.getcwd()}\\Tests"])
        print("Finished Debug Mode")


if __name__ == '__main__':
    run()

# def main():
#     RunTests()


# if __name__ == "__main__":
#     main()
