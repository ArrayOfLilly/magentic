#!/bin/zsh

# Remove the new_dir directory and its contents
rm -rf calculator/new_dir

# Remove test_output.txt in calculator root
rm -f calculator/test_output.txt

# Remove test_output.txt in calculator/pkg
rm -f calculator/pkg/test_output.txt

echo "Test output files and directories cleaned up."