from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

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


def extract(processor: DataProcessor, count: int, label: str) -> None:
    plural = "value" if count == 1 else "values"
    print(f"Extracting {count} {plural}...")
    for _ in range(count):
        rank, value = processor.output()
        print(f"{label} {rank}: {value}")


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    print("\nTesting Numeric Processor...")
    numeric = NumericProcessor()
    for sample in (42, "Hello"):
        print(f"Trying to validate input '{sample}': "
              f"{numeric.validate(sample)}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")
    except ValueError as error:
        print(f"Got exception: {error}")
    numbers: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {numbers}")
    numeric.ingest(numbers)
    extract(numeric, 3, "Numeric value")

    print("\nTesting Text Processor...")
    text = TextProcessor()
    print(f"Trying to validate input '42': {text.validate(42)}")
    words = ["Hello", "Nexus", "World"]
    print(f"Processing data: {words}")
    text.ingest(words)
    extract(text, 1, "Text value")

    print("\nTesting Log Processor...")
    log = LogProcessor()
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")
    logs = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f"Processing data: {logs}")
    log.ingest(logs)
    extract(log, 2, "Log entry")


if __name__ == "__main__":
    main()
