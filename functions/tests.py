import unittest
from get_files_info import get_files_info
from get_file_content import get_file_content

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

print("Testing get_files_info function:")
print("**********************************************************************")
print("Result for current directory:")
print(get_files_info("calculator", "."))
print("----------------------------------------------------------------------")
print("Result for 'pkg' directory:")
print(get_files_info("calculator", "pkg"))
print("----------------------------------------------------------------------")
print("Result for '/bin' directory:")
print(get_files_info("calculator", "/bin"))
print("----------------------------------------------------------------------")
print("Result for '../' directory:")
print(get_files_info("calculator", "../"))
print("")
print("")


class TestGetFileContent(unittest.TestCase):
    
    def test_valid_file(self):
        result = get_file_content("calculator", "lorem.txt")
        self.assertTrue(result.startswith("Lorem ipsum"))
        
    def test_nonexistent_file(self):
        result = get_file_content("calculator", "nonexistent.txt")
        self.assertEqual(result, 'Error: File not found or is not a regular file: "nonexistent.txt"')
        
    def test_directory(self):
        result = get_file_content("calculator", "pkg")
        self.assertEqual(result, 'Error: File not found or is not a regular file: "pkg"')
        
    def test_outside_working_directory(self):
        result = get_file_content("calculator", "../somefile.txt")
        self.assertEqual(result, 'Error: Cannot read "/Users/ArrayOfLilly/workspace/github.com/ArrayOfLilly/magentic/somefile.txt" as it is outside the permitted working directory')
        
    def test_large_file_truncation(self):
        # Assuming lorem.txt is less than MAX_READ_SIZE for this test
        result = get_file_content("calculator", "lorem.txt")
        self.assertIn("[...File \"lorem.txt\" truncated at 10000 characters]", result)
    
print("Testing get_file_content function:")    
print("**********************************************************************")
print(get_file_content("calculator", "lorem.txt"))
print("----------------------------------------------------------------------") 
print(get_file_content("calculator", "nonexistent.txt"))
print("----------------------------------------------------------------------")
print(get_file_content("calculator", "../../../somefile.txt"))
print("----------------------------------------------------------------------")
print(get_file_content("calculator", "lorem.txt")[-51:])  # Print last 50 characters to check truncation message


if __name__ == "__main__":
    unittest.main()