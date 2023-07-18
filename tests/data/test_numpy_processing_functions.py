import numpy as np
import pandas as pd
import pytest
from pytest import approx
from data.numpy_processing_functions import *


class TestNumpyProcessingFunctions:
    def test_convert_file_to_pd_df(self):
        csv_file = 'src/data/Sample_Data.csv'
        df = convert_file_to_pd_df(csv_file)
        assert isinstance(df, pd.DataFrame), "Returned object is not a DataFrame."

    def test_group_data_by_target(self):
        df = convert_file_to_pd_df('src/data/Sample_Data.csv')
        grouped_data = group_data_by_target(df)
        assert isinstance(grouped_data[0], pd.DataFrame), "Returned object is not a DataFrame."
        assert isinstance(grouped_data[1], pd.DataFrame), "Returned object is not a DataFrame."

    def test_summarize_dataset(self):
        csv_file = 'src/data/Sample_Data.csv'
        df = convert_file_to_pd_df(csv_file)
        grouped_data = group_data_by_target(df)
        target_index = 1
        mean, std = summarize_dataset(grouped_data, target_index)
        assert mean["glucose"] == approx(45.0)
        assert mean["bloodpressure"] == approx(66.0)
        assert std["glucose"] == approx(14.719601)
        assert std["bloodpressure"] == approx(4.760952)


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
