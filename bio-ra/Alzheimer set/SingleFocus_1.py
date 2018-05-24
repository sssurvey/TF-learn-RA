import numpy as np
import pandas as pd
# import seaborn as sns
import matplotlib.pyplot as plt
import pylab
# import openpyxl as oxl

def openExcelSheet(path, sheet_name):
    dataframe_excel = pd.read_excel(path, sheet_name)
    print (dataframe_excel)  
    print ("------------clincal diagnosis------------")
    print (dataframe_excel["dcfdx"])  
    return dataframe_excel

def analysis_1(df):
    tmp_df = df[df.columns[5:89]]
    print (tmp_df)
    plt.figure(); tmp_df.plot()
    plt.show()

def analysis_2(df):
    for i in range(5,89):
        print (df[df.columns[i]])
        temp_df = df[df.columns[i]]
        plt.figure(); temp_df.plot()
    plt.show()

def analysis_3(df):
    temp_df = df.copy()
    column_names = list(temp_df.columns.values)
    monitor_dict = {}
    for i in range(4,89):
        change = float(temp_df.iloc[-1,i]) - float(temp_df.iloc[0,i])
        # need to deal with NaN
        # print(change)
        monitor_dict[i] = change
    return monitor_dict

        


def main():
    df_1 = openExcelSheet(
        '/Users/haominshi/Desktop/al_data/individual.xlsx',sheet_name="Sheet1")
    df_2 = openExcelSheet(
        '/Users/haominshi/Desktop/al_data/individual.xlsx', sheet_name="Sheet2")
    # analysis_1(df_1)
    df_dict_1 = analysis_3(df_1)
    print (df_dict_1)
    df_dict_2 = analysis_3(df_2)
    print (df_dict_2)
    # analysis_2(df_1)

if __name__ == "__main__":
    main()
