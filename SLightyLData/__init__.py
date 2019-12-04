'''
Collection of DS functions for ease of access and use!
'''

import pandas as pd
import numpy as np


class SlightyFuncs:
    """
    Functions I've found myself returning to time after time
    """

    def na_sums(self, df):
        """ 
        Provides quick access to each columns total number of NA vals
        """
        # Print a quick view of each columns n/a count
        print(df.isna().sum())

    def dt_split(self, df, column):
        """ 
        When provided a single column of a DataFrame, dt_split will return
        new columns for day, month, and year.
        """

        # Confirm that column name is in string format
        assert type(column) == str

        # Convert column data to datetime format
        df[column] = pd.to_datetime(df[column], infer_datetime_format=True)

        # Extract components & return new columns
        df['Year'] = pd.to_datetime(df[column_name]).dt.year
        df['Month'] = pd.to_datetime(df[column_name]).dt.month
        df['Day'] = pd.to_datetime(df[column_name]).dt.day

        # Drop the now redundant column
        df.drop(columns=column)

        return df

