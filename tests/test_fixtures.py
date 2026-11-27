from pathlib import Path

from src.files import receipt_path


def test_receipt_path_returns_a_path_object():
    if not isinstance(receipt_path("receipt.txt"), Path):
        raise AssertionError("receipt_path should return a Path object")
