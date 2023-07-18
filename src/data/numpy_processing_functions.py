import numpy.typing as np
from typing import List
import pandas as pd


# def create_sample_data(df):
#     sample_data = df.head(9)
#     sample_data.to_csv('Sample_Data.csv', index = False)

# df = convert_file_to_pd_df('Naive-Bayes-Classification-Data.csv')
# create_sample_data(df)
def convert_file_to_pd_df(filepath):
    """
    reads the csv file and converts it to Pandas dataframe
    :return: pd.DataFrame
    """
    df = pd.read_csv(filepath)
    return df


def group_data_by_target(df):
    """
    grouping by the last column (target)
    returns separate DataFrame for target == 0 and target == 1
    """
    target_column = df.columns[-1]
    target = df[target_column]
    grouped = df.groupby(target)
    # create a dictionary to store the resulting DataFrames
    result = {}
    for group_name, group_df in grouped:
        # Drop the target column from the group DataFrame
        group_df = group_df.drop([target_column], axis=1)

        # Store the group DataFrame in the result dictionary
        result[group_name] = group_df
    return result


# df = convert_file_to_pd_df('Sample_Data.csv')
# grouped_data = group_data_by_target(df)
# print("Group 0")
# print(grouped_data[0])
# print("Group 1")
# print(grouped_data[1])


def summarize_dataset(grouped_data, index):
        """
        Calculates the mean and standard deviation for a specific DataFrame in a grouped data dictionary.
        Returns the mean and standard deviation values for the DataFrame at the specified index.
        """
        df = grouped_data[index]
        mean = df.mean()
        std = df.std()
        return mean, std

# df = convert_file_to_pd_df('Sample_Data.csv')
# grouped_data = group_data_by_target(df)
#
# # Specify the target DataFrame index
# target_index = 1
#
# # Calculate statistics for the target DataFrame
# mean, std = summarize_dataset(grouped_data, target_index)
#
# # Print the mean and standard deviation for the target DataFrame
# print(f"Mean for the target {target_index} DataFrame:")
# print(mean["glucose"])
# print(mean["bloodpressure"])
# print()
#
# print(f"Standard deviation for the target {target_index} DataFrame:")
# print(std)





def select_rows(arr: np.ArrayLike, indices: List[int]) -> np.ArrayLike:
    """
    :type indices: list
    :type arr: np.Array
    :param arr: np.array([
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 0]
    ])
    :param indices:[0,2]
    :return:np.array([
    [1, 0, 0, 1],
    [1, 0, 1, 0]
    ])
    """
    return arr[indices]


def make_labels_dict(labels: List[int | str]) -> dict:
    """
    :param labels: [0, 1, 1, 0, 1]
    :return: {0: [0, 3], 1: [1, 2, 4]}
    """
    label_dict = {}
    for index, label in enumerate(labels):
        if label not in label_dict:
            label_dict[label] = []
        label_dict[label].append(index)
    return label_dict
