from printer.logger import Logger


class FileLogger(Logger):
    def __init__(self, file_name: str):
        with open(file_name, "w+", encoding='utf-8') as file:
            self.file = file

    def normal(self, message: str) -> None:
        self.file.write(f"{message}\n")

    def debug(self, message: str) -> None:
        self.file.write(f"{{DEBUG}}: {message}\n")

    def error(self, message: str) -> None:
        self.file.write(f"{{ERROR}}: {message}\n")

    def info(self, message: str) -> None:
        self.file.write(f"{{INFO}}: {message}\n")

    def __del__(self):
        self.file.close()
