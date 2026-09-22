from abc import ABC, abstractmethod
from typing import Any, Protocol


class DataProcessor(ABC):

    name: str = "Data Processor"

    def __init__(self) -> None:
        self.storage: list[tuple[int, str]] = []
        self.rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def store(self, item: str) -> None:
        self.storage.append((self.rank, item))
        self.rank += 1

    def output(self) -> tuple[int, str]:
        if not self.storage:
            raise IndexError("No data left to output")
        return self.storage.pop(0)


class NumericProcessor(DataProcessor):

    name = "Numeric Processor"

    @staticmethod
    def is_number(value: Any) -> bool:
        return isinstance(value, (int, float)) and not isinstance(value, bool)

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(self.is_number(item) for item in data)
        return self.is_number(data)

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self.store(str(item))


class TextProcessor(DataProcessor):

    name = "Text Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return isinstance(data, str)

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self.store(item)


class LogProcessor(DataProcessor):

    name = "Log Processor"

    @staticmethod
    def is_log(value: Any) -> bool:
        return isinstance(value, dict) and all(
            isinstance(key, str) and isinstance(val, str)
            for key, val in value.items()
        )

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(self.is_log(item) for item in data)
        return self.is_log(data)

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self.store(": ".join(item.values()))


class ExportPlugin(Protocol):

    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExportPlugin:

    @staticmethod
    def escape(value: str) -> str:
        if any(char in value for char in ',"\n\r'):
            return '"' + value.replace('"', '""') + '"'
        return value

    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        print(",".join(self.escape(value) for _, value in data))


class JSONExportPlugin:

    @staticmethod
    def escape(value: str) -> str:
        result = ""
        for char in value:
            if char == '"':
                result += '\\"'
            elif char == "\\":
                result += "\\\\"
            elif char == "\n":
                result += "\\n"
            elif char == "\r":
                result += "\\r"
            elif char == "\t":
                result += "\\t"
            elif ord(char) < 0x20:
                result += f"\\u{ord(char):04x}"
            else:
                result += char
        return '"' + result + '"'

    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        pairs = [
            f"{self.escape(f'item_{rank}')}: {self.escape(value)}"
            for rank, value in data
        ]
        print("{" + ", ".join(pairs) + "}")


class DataStream:

    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        if proc not in self.processors:
            self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            for proc in self.processors:
                if proc.validate(element):
                    proc.ingest(element)
                    break
            else:
                print("DataStream error - "
                      f"Can't process element in stream: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            print(f"{proc.name}: total {proc.rank} items "
                  f"processed, remaining {len(proc.storage)} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            count = min(nb, len(proc.storage))
            data = [proc.output() for _ in range(count)]
            if data:
                plugin.process_output(data)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")

    print("Initialize Data Stream...\n")
    stream = DataStream()
    stream.print_processors_stats()
    print()

    print("Registering Processors\n")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    batch: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO",
             "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {batch}\n")
    stream.process_stream(batch)
    stream.print_processors_stats()
    print()

    print("Send 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVExportPlugin())
    print()
    stream.print_processors_stats()

    batch = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR",
             "log_message": "500 server crash"},
            {"log_level": "NOTICE",
             "log_message": "Certificate expires in 10 days"},
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]
    print()
    print(f"Send another batch of data: {batch}")
    print()
    stream.process_stream(batch)
    stream.print_processors_stats()
    print()

    print("Send 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONExportPlugin())
    print()
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
