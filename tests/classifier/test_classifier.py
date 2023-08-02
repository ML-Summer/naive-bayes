import pytest
import pandas
from classifier.classifier import bayesClassifier

class TestClassifier:
    def test_incompatibile_data_sample_bigger(self):
        train = pandas.DataFrame([[1,2], [3,4]])
        sample = [5, 6]
        with pytest.raises(ValueError):
            bayesClassifier(train, sample)
    def test_incompatibile_data_sample_smaller(self):
        train = pandas.DataFrame([[1, 2, 3], [3, 4, 5]])
        sample = [5]
        with pytest.raises(ValueError):
            bayesClassifier(train, sample)

pytest.main()