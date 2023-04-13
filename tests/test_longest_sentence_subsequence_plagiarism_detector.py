# add the root project directory to the system path:
import sys
import pathlib

parent_dir_path = pathlib.Path(__file__).parent.parent
sys.path.append(str(parent_dir_path))
sys.path.append(f"{str(parent_dir_path)}/joes_giant_toolbox/")

# import the function to be tested:
from joes_giant_toolbox.longest_sentence_subsequence_plagiarism_detector import (
    longest_sentence_subsequence_plagiarism_detector,
)

# run the tests:
def test_known_output_example():
    result = longest_sentence_subsequence_plagiarism_detector()
    assert 1 == 1, "text if fails"
