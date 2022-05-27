

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def open_csv(file_name):
    # open csv file
    df = pd.read_csv(file_name)
    return df


def check_failed_attempts(df):
    # checking if the is_successful_payment is 0 and failed_attempts is equal to 1
    df_failed = df[(df['is_successful_payment'] == 0) & (df['failed_attempts'] == 1)]
    return df_failed

def check_multiple_failed_attempt(df):
    # checking if the is_successful_payment is 0 and failed_attempts is equal to or more than 2
    df_multiple_attempt_failed = df[(df['is_successful_payment'] == 0) & (df['failed_attempts'] >= 2)]
    return df_multiple_attempt_failed

def check_multiple_attempt_succeeded(df):
    # checking if the is_successful_payment is 0 and failed_attempts is equal to or more than 2
    df_multiple_attempt_succeeded = df[(df['is_successful_payment'] == 1) & (df['failed_attempts'] >= 2)]
    return df_multiple_attempt_succeeded



def main():
    df = open_csv('bolt.csv')
    df_failed = check_failed_attempts(df)
    print("Number of failed attempts on first trial: ", len(df_failed))
    print(df_failed)
    df_multiple_attempt_failed = check_multiple_failed_attempt(df)
    print("Number of multiple failed attempts after first trial: ", len(df_multiple_attempt_failed))
    print(df_multiple_attempt_failed)
    print("Number of multiple failed attempts after first trial and succeeded: ", len(check_multiple_attempt_succeeded(df)))
    print(check_multiple_attempt_succeeded(df))
    plt.show()


if __name__ == '__main__':
    main()







