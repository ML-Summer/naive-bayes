from math import sqrt, exp, pi
from pandas import DataFrame
from typing import List
from data.numpy_processing_functions import group_data_by_target


def getNormalDistribution(distribution_parameters: tuple[float] | list[float]):
    """
    Returns a callable lambda function of normal distribution's PDF.
    # Parameters
    - `distribution_parameters` - list of distribution's parameters, mean and standard deviation(in that order)
    # Returns
    - a lambda function that takes an `x` argument and returns this argument's value from Gaussian PDF.
    """
    mean = distribution_parameters[0]
    std = distribution_parameters[1]
    return lambda x: 1 / (std * sqrt(2 * pi)) * exp(-(1 / 2) * ((x - mean) / std) ** 2)

def getPrior(train: DataFrame) -> dict:
    """
    Computes prior for every column and label.
    # Parameters

    - `train` - dataframe that contains feature data.

    # Returns

    Dict with list of prior probabilities for label.
    """
    train_column_length = float(len(train))
    train_sorted = group_data_by_target(train)
    prior = {}
    for key, frame in train_sorted.items():
        prior[key] = round(float(len(frame)) / train_column_length, 4)
    return prior