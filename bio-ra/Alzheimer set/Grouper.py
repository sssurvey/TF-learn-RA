import numpy as np
import pandas as pd
# import seaborn as sns
import matplotlib.pyplot as plt
import pylab
# import openpyxl as oxl
import SingleFocus_1 as sf1
import Dropper as dropper
import time as t


'''
the purpose of this file is to scan the csv
then group the subject based on their ID number
create a list of df that each df is one patient
with 2 group:
    1. was diagnosed
    2. was not diagnosed
'''
def grouping(df):
    """
    create a list of dataframes, each element of the list contains a dataframe
    that is grouped by ID
    """
    # convert the values from the projid to a list
    projid_list = df.projid.unique()
    projid_list = projid_list.tolist() #list acquired this is a unique list of ID

    list_of_patients = []
    counter_start_df_row = 0 # used for slicing the df, first
    counter_end_df_row   = 0 # used for slicing the df, last
    df = df.reset_index(drop = True) # df reindexed
    row_count = df.shape[0]
    # df_index = 0


    # !!! problem horrible efficiency, need fix suspect df_index for loop issue
    for p_id in projid_list: # loop through the unique id list
        for df_index in range(0, row_count):
            if df.iloc[df_index]['projid'] == p_id:
                counter_end_df_row += 1
            elif df.iloc[df_index]['projid'] != p_id:
                print ("List appended ===>>> " + str(p_id))
                continue
        list_of_patients.append(df[counter_start_df_row: counter_end_df_row])
        counter_start_df_row = counter_end_df_row
    # print (list_of_patients) CHECKED
    return list_of_patients # a list of df, that each element of the list is one patient

def main():
    path = '/Users/haominshi/Desktop/al_data/dataset_576_long.xlsx'
    path_test = '/Users/haominshi/Desktop/al_data/dataset_testing_short.xlsx'
    timer_1 = t.time()

    # =============================== Change path here
    data_set_everything = sf1.openExcelSheet(path, sheet_name="Sheet0")
    # data_set_everything = sf1.openExcelSheet(path_test, "Sheet1")
    # ==========================================================================
    
    # ==========================================================================
    timer_1 = t.time() - timer_1
    print (timer_1)
    print (data_set_everything.shape)
    # file transfered to DF
    timer_1 = t.time()
    # ==========================================================================
    data_set_everything = dropper.drop_none_important_features(data_set_everything)
    # drop none important features
    data_set_everything = dropper.clean_history(data_set_everything)
    # ==========================================================================
    timer_1 = t.time() - timer_1
    print(timer_1)
    print(data_set_everything.shape)
    data_set_cleaned = data_set_everything.copy()
    # ==========================================================================
    timer_1 = t.time()
    # list_of_patient = list of df based on each patient, each element of the list
    # is a patient, and in that patient, we have the DF for each of their visit
    list_of_patient = grouping(data_set_cleaned)
    timer_1 = t.time() - timer_1
    # ==========================================================================


if __name__ == "__main__":
    main()
