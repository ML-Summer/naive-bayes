import pytest
from pytest import approx
from analysis.probability_calc import getNormalDistribution

#test values source: https://www.danielsoper.com/statcalc/calculator.aspx?id=54

class TestProbabilityCalculationFunctions:
    def test_get_gaussian(self):
        mean = 0
        std = 1
        distribution = getNormalDistribution([mean, std])
        assert distribution(1) == approx(0.24197)
    def test_gaussian_custom_sigma(self):
        mean = 0
        std = 5
        distribution = getNormalDistribution([mean, std])
        assert distribution(3) == approx(0.06664)