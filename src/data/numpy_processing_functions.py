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








