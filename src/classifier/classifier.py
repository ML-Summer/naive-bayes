from analysis.probability_calc import getNormalDistribution
from data.numpy_processing_functions import *
import pandas
from pandas import DataFrame
from typing import Tuple

def bayesClassifier(train: DataFrame, sample: List[float]) -> Tuple[any, dict]:
    """
    Classifies sample based on training data and computes likelihood for each label.
    # Parameters

    - `train` - pandas DataFrame; last column is considered to contain labels.
    - sample - list of feature values.

    # Returns

    A tuple that contains:
    - matched label,
    - dictionary of likelihoods for each label.
    """
    if len(train) is not (len(train.iloc[0]) - 1):
        return ValueError("Train dataset row(without label) and classfied sample vary in lengths")
    