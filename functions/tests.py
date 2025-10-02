import unittest
from get_files_info import get_files_info
from get_file_content import get_file_content
from write_file import write_file

# class TestGetFilesInfo(unittest.TestCase):
    
#     def test_valid_directory(self):
#         result = get_files_info("calculator", ".")
#         self.assertIn("main.py", result)
#         self.assertIn("tests.py", result)
#         self.assertIn("pkg", result)
        
#     def test_subdirectory(self):
#         result = get_files_info("calculator", "pkg")
#         self.assertIn("calculator.py", result)
#         self.assertIn("render.py", result)
        
#     def test_outside_working_directory(self):
#         result = get_files_info("calculator", "/bin")
#         self.assertEqual(result, 'Error: Cannot list "/bin" as it is outside the permitted working directory')

#     def test_parent_directory(self):
#         result = get_files_info("calculator", "../")
#         self.assertEqual(result, 'Error: Cannot list "../" as it is outside the permitted working directory')

# print("Testing get_files_info function:")
# print("**********************************************************************")
# print("Result for current directory:")
# print(get_files_info("calculator", "."))
# print("----------------------------------------------------------------------")
# print("Result for 'pkg' directory:")
# print(get_files_info("calculator", "pkg"))
# print("----------------------------------------------------------------------")
# print("Result for '/bin' directory:")
# print(get_files_info("calculator", "/bin"))
# print("----------------------------------------------------------------------")
# print("Result for '../' directory:")
# print(get_files_info("calculator", "../"))
# print("\n\n")


# class TestGetFileContent(unittest.TestCase):
    
#     def test_valid_file(self):
#         result = get_file_content("calculator", "lorem.txt")
#         self.assertTrue(result.startswith("Lorem ipsum"))
        
#     def test_file_in_subdirectory(self):    
#         result = get_file_content("calculator", "pkg/calculator.py")
#         self.assertIn('"+": lambda a, b: a + b,', result)
        
#     def test_nonexistent_file(self):
#         result = get_file_content("calculator", "nonexistent.txt")
#         self.assertEqual(result, 'Error: File not found or is not a regular file: "nonexistent.txt"')
        
#     def test_directory(self):
#         result = get_file_content("calculator", "pkg")
#         self.assertEqual(result, 'Error: File not found or is not a regular file: "pkg"')
        
#     def test_outside_working_directory(self):
#         result = get_file_content("calculator", "../somefile.txt")
#         self.assertEqual(result, 'Error: Cannot read "/Users/ArrayOfLilly/workspace/github.com/ArrayOfLilly/magentic/somefile.txt" as it is outside the permitted working directory')
        
#     def test_large_file_truncation(self):
#         result = get_file_content("calculator", "lorem.txt")
#         self.assertIn("[...File \"lorem.txt\" truncated at 10000 characters]", result)
    
# print("Testing get_file_content function:")    
# print("**********************************************************************")
# print(get_file_content("calculator", "lorem.txt"))
# print("----------------------------------------------------------------------") 
# print(get_file_content("calculator", "pkg/calculator.py"))
# print("----------------------------------------------------------------------")
# print(get_file_content("calculator", "nonexistent.txt"))
# print("----------------------------------------------------------------------")
# print(get_file_content("calculator", "../../../somefile.txt"))
# print("----------------------------------------------------------------------")
# print(get_file_content("calculator", "lorem.txt")[-51:])
# print("\n\n")

class TestWriteFile(unittest.TestCase):
    
    def test_write_valid_file(self):
        result = write_file("calculator", "test_output.txt", "Hello, World!")
        self.assertEqual(result, 'Successfully wrote to "test_output.txt" (13 characters written)')
        content = get_file_content("calculator", "test_output.txt")
        self.assertEqual(content, "Hello, World!")
        
    def test_write_in_subdirectory(self):
        result = write_file("calculator", "pkg/test_output.txt", "Hello, Subdirectory!")
        self.assertEqual(result, 'Successfully wrote to "pkg/test_output.txt" (20 characters written)')
        content = get_file_content("calculator", "pkg/test_output.txt")
        self.assertEqual(content, "Hello, Subdirectory!")
        
    def test_write_outside_working_directory(self):
        result = write_file("calculator", "../outside.txt", "This should fail.")
        self.assertEqual(result, 'Error: Cannot write to "../outside.txt" as it is outside the permitted working directory')
        
    def test_write_in_nonexistent_subdirectory(self):
        result = write_file("calculator", "new_dir/test_output.txt", "Hello, New Directory!")
        self.assertEqual(result, 'Successfully wrote to "new_dir/test_output.txt" (21 characters written)')
        content = get_file_content("calculator", "new_dir/test_output.txt")
        self.assertEqual(content, "Hello, New Directory!")
        
print("Testing write_file function:")
print("**********************************************************************")
print(write_file("calculator", "test_output.txt", "Hello, World!"))
print("Contents of 'test_output.txt':")
print(get_file_content("calculator", "test_output.txt"))
print("----------------------------------------------------------------------")
print(write_file("calculator", "pkg/test_output.txt", "Hello, Subdirectory!"))
print("Contents of 'pkg/test_output.txt':")
print(get_file_content("calculator", "pkg/test_output.txt"))
print("----------------------------------------------------------------------")
print(write_file("calculator", "../outside.txt", "This should fail."))
print("----------------------------------------------------------------------")
print(write_file("calculator", "new_dir/test_output.txt", "Hello, New Directory!"))
print("Contents of 'new_dir/test_output.txt':")
print(get_file_content("calculator", "new_dir/test_output.txt"))
print("\n\n")

if __name__ == "__main__":
    unittest.main()