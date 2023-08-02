import pytest
from pytest import approx
from analysis.probability_calc import getNormalDistribution, getPrior
from data.data_processing_functions import convert_file_to_pd_df

#test values source: https://www.danielsoper.com/statcalc/calculator.aspx?id=54

class TestProbabilityCalculationFunctions:
    def test_get_gaussian(self):
        mean = 0
        std = 1
        distribution = getNormalDistribution([mean, std])
        assert distribution(1) == approx(0.24197072)
    def test_gaussian_custom_sigma(self):
        mean = 0
        std = 5
        distribution = getNormalDistribution([mean, std])
        assert distribution(3) == approx(0.06664492)
    def test_prior_calc(self):
        train = convert_file_to_pd_df('src/data/Sample_Data.csv')
        expected_data = {
            0: 0.5556,
            1: 0.4444
        }
        assert getPrior(train) == expected_data