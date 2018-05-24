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
    """this is a time based analyis to see what changed during the visit"""
    tmp_df = df[df.columns[5:89]]
    print (tmp_df)
    plt.figure(); tmp_df.plot()
    plt.show()

def analysis_2(df):
    """find corralations"""
    for i in range(5,90):
        print (df[df.columns[i]])
        temp_df = df[df.columns[i]]
        plt.figure(); temp_df.plot()
    plt.show()
        


def main():
    df_1 = openExcelSheet('/Users/haominshi/Desktop/al_data/individual.xlsx',sheet_name="Sheet1")
    analysis_1(df_1)
    analysis_2(df_1)

if __name__ == "__main__":
    main()
