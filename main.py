from app.io.input import input_from_console, read_from_file_builtin, read_from_file_with_pandas
from app.io.output import output_to_console, write_to_file_builtin


def main():
    text_from_console = input_from_console()

    file_path_builtin = "data/example_builtin.txt"
    content_from_file_builtin = read_from_file_builtin(file_path_builtin)

    file_path_pandas = "data/example_pandas.csv"
    content_from_file_pandas = read_from_file_with_pandas(file_path_pandas)

    # Вивід результатів у консоль
    output_to_console("Текст з консолі:")
    output_to_console(text_from_console)
    output_to_console("\nЗчитано з файлу (вбудовані можливості Python):")
    output_to_console(content_from_file_builtin)
    output_to_console("\nЗчитано з файлу (бібліотека pandas):")
    output_to_console(content_from_file_pandas)

    output_file_path = "data/output.txt"
    write_to_file_builtin(output_file_path,
                          f"Текст з консолі:\n{text_from_console}\n\nЗчитано з файлу (вбудовані можливості Python):\n{content_from_file_builtin}\n\nЗчитано з файлу (бібліотека pandas):\n{content_from_file_pandas}")
    print(f"Результати були збережені до файлу '{output_file_path}'")


if __name__ == "__main__":
    main()
