import unittest
from app.io.input import read_from_file_builtin, read_from_file_with_pandas


class TestFileReading(unittest.TestCase):
    def test_read_from_file_builtin(self):
        # Тестування зчитування з файлу за допомогою вбудованих можливостей Python
        file_path = "test_file.txt"
        expected_content = "Test content from file"
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(expected_content)
        content = read_from_file_builtin(file_path)
        self.assertEqual(content, expected_content)



if __name__ == "__main__":
    unittest.main()
