import numpy as np
import pandas as pd

#Check a dataframe for nulls, print/report them in a nice "pretty" format
def get_info(dataframe):
    print(dataframe.shape)
    print (dataframe.isna().sum())



#adds a row onto a dataframe that is filled with randomized numbers set by user
def randrow(dataframe, min=0, max=100):
    i=0
    while 'randrow_{}'.format(i) in dataframe.columns:
        i += 1
    dataframe['randrow_{}'.format(i)] = pd.Series(np.random.randint(min, max, size=len(dataframe)))
    return dataframe

'''
#searches for text all throughout data frame and returns row index
def find_text(string, dataframe):
    for col in dataframe:
        for row in dataframe:
            for value in row:
                if value == string:
                    return value.iloc
'''
