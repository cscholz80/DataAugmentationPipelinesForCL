"""Test the structure of the dataaugmentationpipelinesforcl module."""
import unittest
import os


class TestProjectStructure(unittest.TestCase):
    """Test if the structure of the dataaugmentationpipelinesforcl module is correct."""

    def assert_dir(self, dirname):
        return self.assert_(os.path.isdir(dirname))
    def assert_file(self, filename):
        return self.assert_(os.path.isfile(filename))

    def test_scripts_folder_exists(self):
        """Test whether the folder `scripts/` exists."""
        self.assert_dir('./scripts')

    def test_tests_folder_exists(self):
        """Test whether the folder `tests/` exists."""
        self.assert_dir('./tests')
        self.assert_file('./tests/__init__.py')

    def test_docs_folder_exists(self):
        """Test whether the folder `docs/` exists."""
        self.assert_dir('./docs')
        self.assert_file('./docs/conf.py')
        self.assert_file('./docs/index.rst')

    def test_module_folder_exists(self):
        """The whether a folder for the module exists."""
        path = './dataaugmentationpipelinesforcl'
        self.assert_dir(path)
        self.assert_file(os.path.join(path, '__init__.py'))

    def test_rootlevel_files_exist(self):
        """Test whether all the root level files we need exists."""
        self.assert_file('./setup.py')
        self.assert_file('./README.rst')
        self.assert_file('./LICENSE.txt')
        self.assert_file('.gitignore')

if __name__ == '__main__':
    unittest.main()
