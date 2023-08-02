import numpy.typing as np
from typing import List
import pandas as pd



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




def summarize_dataset(grouped_data, index):
        """
        Calculates the mean and standard deviation for a specific DataFrame in a grouped data dictionary.
        Returns the mean and standard deviation values for the DataFrame at the specified index.
        """
        df = grouped_data[index]
        mean = df.mean()
        std = df.std()
        return mean, std










