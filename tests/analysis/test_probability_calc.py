import pytest
from analysis.probability_calc import getNormalDistribution

#test values source: https://www.danielsoper.com/statcalc/calculator.aspx?id=54

class TestProbabilityCalculationFunctions:
    def test_get_gaussian(self):
        mu = 0
        sigma = 1
        distribution = getNormalDistribution(mu, sigma)
        assert distribution(1) == 0.24197