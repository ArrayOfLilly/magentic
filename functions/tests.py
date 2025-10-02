import unittest
from get_files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):
    
    def test_valid_directory(self):
        result = get_files_info("calculator", ".")
        self.assertIn("main.py", result)
        self.assertIn("tests.py", result)
        self.assertIn("pkg", result)
        
    def test_subdirectory(self):
        result = get_files_info("calculator", "pkg")
        self.assertIn("calculator.py", result)
        self.assertIn("render.py", result)
        
    def test_outside_working_directory(self):
        result = get_files_info("calculator", "/bin")
        self.assertEqual(result, 'Error: Cannot list "/bin" as it is outside the permitted working directory')

    def test_parent_directory(self):
        result = get_files_info("calculator", "../")
        self.assertEqual(result, 'Error: Cannot list "../" as it is outside the permitted working directory')

print("----------------------------------------------------------------------")
print(get_files_info("calculator", "."))
print("----------------------------------------------------------------------")
print(get_files_info("calculator", "pkg"))
print("----------------------------------------------------------------------")
print(get_files_info("calculator", "/bin"))
print("----------------------------------------------------------------------")
print(get_files_info("calculator", "../"))
print("----------------------------------------------------------------------")

if __name__ == "__main__":
    unittest.main()