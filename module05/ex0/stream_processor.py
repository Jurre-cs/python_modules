from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self):
        self.data: list[tuple[int, str]] = []
        self.next_rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        item = self.data.pop(0)
        return item


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, bool):
            return False
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(
                not isinstance(i, bool) and isinstance(i, (int, float))
                for i in data
            )
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self.data.append((self.next_rank, str(item)))
            self.next_rank += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and all(isinstance(i, str) for i in data):
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self.data.append((self.next_rank, item))
            self.next_rank += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def is_str_str_dict(d):
            return isinstance(d, dict) \
                and all(isinstance(k, str) for k in d.keys()) \
                and all(isinstance(v, str) for v in d.values())

        if is_str_str_dict(data):
            return True
        if isinstance(data, list) and all(is_str_str_dict(d) for d in data):
            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            level = item.get("log_level", "").strip()
            message = item.get("log_message", "").strip()
            formatted = f"{level}: {message}"
            self.data.append((self.next_rank, formatted))
            self.next_rank += 1


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")

    print("Testing Numeric Processor...")
    np = NumericProcessor()
    print(f"Trying to validate input '42': {np.validate(42)}")
    print(f"Trying to validate input 'Hello': {np.validate('Hello')}")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        np.ingest("foo")
    except Exception as e:
        print(f"Got exception: {e}")

    data = [1, 2, 3, 4, 5]
    print(f"Processing data: {data}")
    np.ingest(data)
    print("Extracting 3 values...")
    for _ in range(3):
        rank, value = np.output()
        print(f"Numeric value {rank}: {value}")

    print("\nTesting Text Processor...")
    tp = TextProcessor()
    print(f"Trying to validate input '42': {tp.validate(42)}")
    text_data = ["Hello", "Nexus", "World"]
    print(f"Processing data: {text_data}")
    tp.ingest(text_data)
    print("Extracting 1 value...")
    for _ in range(1):
        rank, value = tp.output()
        print(f"Text value {rank}: {value}")

    print("\nTesting Log Processor...")
    lp = LogProcessor()
    print(f"Trying to validate input 'Hello': {lp.validate('Hello')}")
    log_data = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR ", "log_message": "Unauthorized access!!"},
    ]
    print(f"Processing data: {log_data}")
    lp.ingest(log_data)
    print("Extracting 2 values...")
    for _ in range(2):
        rank, value = lp.output()
        print(f"Log entry {rank}: {value}")
