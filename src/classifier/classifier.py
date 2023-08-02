from analysis.probability_calc import getNormalDistribution, getPrior
from data.numpy_processing_functions import *
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
    if len(sample) is not (len(train.iloc[0]) - 1):
        raise ValueError(
            "Train dataset row(without label) and classfied sample vary in lengths"
            )
    grouped_train = group_data_by_target(train)
    prior = getPrior(train)
    likelihoods = {}
    distributions = {}
    labels = grouped_train.keys()
    for label in labels:
        mean, std = summarize_dataset(grouped_train, label)
        column_labels = mean.keys()
        distribution_params = []
        for column_label in column_labels:
            distribution_params.append(
                [mean[column_label], std[column_label]]
            )
        distributions[label] = distribution_params
    for label in labels:
        label_pdfs = []
        for distribution_param in distributions[label]:
            label_pdfs.append(getNormalDistribution(distribution_param))
        label_likelihood = prior[label]
        for feature, pdf in enumerate(label_pdfs):
            label_likelihood = label_likelihood * pdf(sample[feature])
        likelihoods[label] = label_likelihood
    likelihood_sum = sum(likelihoods.values())
    for label, likelihood in likelihoods.items():
        likelihoods[label] = likelihood/likelihood_sum
    classification = max(likelihoods)
    return (classification, likelihoods)