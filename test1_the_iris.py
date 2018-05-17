import openpyxl
import sys
from sklearn import tree

dataSet_iris_flower = openpyxl.load_workbook('test_data_sets/fishers_iris_data.xlsx')
sheet1 = dataSet_iris_flower['Sheet1']

def analysisData(sheet1):
    
    """features = []
    labels = []
    clf = tree.DecisionTreeClassifier(features,labels)
    clf = clf.fit(features,labels)
"""