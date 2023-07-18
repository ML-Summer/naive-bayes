import numpy as np
import pytest
from data.numpy_processing_functions import select_rows, make_labels_dict


class TestNumpyProcessingFunctions:
    def test_select_rows(self):
        arr = np.array([
            [1, 0, 0, 1],
            [1, 1, 0, 1],
            [1, 0, 1, 0],
            [1, 1, 0, 0]])
        indices = [0, 2]

        expected_result = np.array([[1, 0, 0, 1], [1, 0, 1, 0]])
        actual_result = select_rows(arr, indices)
        assert np.array_equal(actual_result, expected_result)

    def test_make_labels_dict(self):
        labels = [0, 1, 1, 0, 1]
        expected_result = {0: [0, 3], 1: [1, 2, 4]}
        actual_result = make_labels_dict(labels)
        assert expected_result == actual_result


pytest.main()
