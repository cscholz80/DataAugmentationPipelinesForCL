import pytest
import tempfile
import os

# Import the function you want to test
from dataaugmentationpipelinesforcl.helper import extract_primary


def test_extract_primary_valid():
    """
    Test case for a valid input filename with a '/' character.
    """
    input_filename = "vibsta2/vibsta2_XC342263_3.ogg"
    expected_output = "vibsta2"

    assert extract_primary(input_filename) == expected_output


def test_extract_primary_no_separator():
    """
    Test case for an input filename without a '/' character.
    """
    input_filename = "filename.txt"

    with pytest.raises(ValueError) as exc_info:
        extract_primary(input_filename)

    assert str(exc_info.value) == "Input filename must contain a '/' character."


def test_extract_primary_empty_input():
    """
    Test case for an empty input filename.
    """
    input_filename = ""

    with pytest.raises(ValueError) as exc_info:
        extract_primary(input_filename)

    assert str(exc_info.value) == "Input filename must contain a '/' character."


def test_extract_primary_only_separator():
    """
    Test case for an input filename with only a '/' character.
    """
    input_filename = "/"
    expected_output = ""

    assert extract_primary(input_filename) == expected_output


def test_extract_primary_multiple_separators():
    """
    Test case for an input filename with multiple '/' characters.
    """
    input_filename = "/path/to/directory/"
    expected_output = "/path"

    assert extract_primary(input_filename) == expected_output


def test_extract_primary_temp_file():
    """
    Test case for a temporary file with a '/' character in its name.
    """
    # Create a temporary directory and file with a '/' character in the filename
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_filename = os.path.join(temp_dir, "file/1.txt")
        open(temp_filename, "w").close()

        # Expected output is the directory path before the first '/'
        expected_output = temp_dir

        assert extract_primary(temp_filename) == expected_output
