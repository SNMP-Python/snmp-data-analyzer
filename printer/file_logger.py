from printer.logger import Logger


class FileLogger(Logger):

    def __init__(self, file_name: str, debug: bool):
        # pylint: disable=R1732
        self.file = open(file_name, "w+", encoding='utf8')
        super().__init__(debug)

    def normal(self, message: str) -> None:
        self.file.write(f"{message}\n")

    def _debug_impl(self, message: str) -> None:
        self.file.write(f"{{DEBUG}}: {message}\n")

    def error(self, message: str) -> None:
        self.file.write(f"{{ERROR}}: {message}\n")

    def info(self, message: str) -> None:
        self.file.write(f"{{INFO}}: {message}\n")

    def __del__(self):
        self.file.close()
