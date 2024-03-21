def output_to_console(text):
    """
    Функція для виводу тексту у консоль.

    Параметри:
        text (str): Текст, який потрібно вивести у консоль.
    """
    print(text)


def write_to_file_builtin(file_path, content):
    """
    Функція для запису до файлу за допомогою вбудованих можливостей Python.

    Параметри:
        file_path (str): Шлях до файлу, в який потрібно записати.
        content (str): Вміст, який потрібно записати до файлу.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


