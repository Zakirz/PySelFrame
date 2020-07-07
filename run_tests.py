from Core.BrowserHelpers import BrowserHelpers


class RunTests(BrowserHelpers):
    def __init__(self):
        try:
            self.start_execution()
        finally:
            self.stop_execution()


def main():
    RunTests()


if __name__ == "__main__":
    main()
