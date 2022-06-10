from printer.logger import Logger

SUCCESS = "\033[0;32m"
DEBUG = "\033[0;33m"
ERROR = "\033[0;31m"
END_COLOR = "\033[0m"


class StdoutLogger(Logger):
    def normal(self, message: str) -> None:
        print(message)

    def _debug_impl(self, message: str) -> None:
        print(f"{DEBUG}{{debug}}{END_COLOR}: {message}")

    def error(self, message: str) -> None:
        print(f"{ERROR}{{error}}{END_COLOR}: {message}")

    def info(self, message: str) -> None:
        print(f"{SUCCESS}{{info}}{END_COLOR}: {message}")
