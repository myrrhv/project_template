import pandas as pd

def input_from_console():
    """
    Функція для вводу тексту з консолі.
    """
    text = input("Введіть текст: ")
    return text


def read_from_file_builtin(file_path):
    """
    Функція для зчитування з файлу за допомогою вбудованих можливостей Python.

    Параметри:
        file_path (str): Шлях до файлу, який потрібно прочитати.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
        return None


def read_from_file_with_pandas(file_path):
    """
    Функція для зчитування з файлу за допомогою бібліотеки pandas.

    Параметри:
        file_path (str): Шлях до файлу, який потрібно прочитати.
    """
    try:
        df = pd.read_csv(file_path)
        return df.to_string(index=False)
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
        return None

