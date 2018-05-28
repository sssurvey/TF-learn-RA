import numpy as np
import pandas as pd
# import seaborn as sns
import matplotlib.pyplot as plt
import pylab
# import openpyxl as oxl
import SingleFocus_1 as sf1
import Dropper as dropper

'''
the purpose of this file is to scan the csv
then group the subject based on their ID number
create a list of df that each df is one patient
with 2 group:
    1. was diagnosed
    2. was not diagnosed
'''


def main():
    path = '/Users/haominshi/Desktop/al_data/dataset_576_long.xlsx'
    data_set_everything = sf1.openExcelSheet(path, sheet_name="Sheet1")
    # file transfered to DF
    data_set_everything = dropper.drop_none_important_features(data_set_everything)
    # drop none important features
    # print(data_set_everything)
    
    







if __name__ == "__main__":
    main()
