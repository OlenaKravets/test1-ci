import csv
import os

def test_csv_file_exists():
    path = "data_tests/sample.csv"
    assert os.path.exists(path), f"❌ CSV файл не знайдено: {path}"

def test_csv_has_columns():
    with open("data_tests/sample.csv", "r") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        for col in ["name", "email", "age"]:
            assert col in headers, f"❌ Колонка '{col}' відсутня"
