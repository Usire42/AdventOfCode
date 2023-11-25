
import pandas as pd
import re

# import content of .txt file

def import_txt(xls_path):
    df = pd.read_excel(xls_path, 'Sheet1', header= None )
    return df

def caloriescounter(xls_path):
    df = import_txt(xls_path)
    elfdict = {}
    elfnumb = 1
    calories = 0
    for i in range(len(df) - 1):
        try:
            value = int(df.at[i, 0])
            calories += value
        except ValueError:
            elfdict[elfnumb] = calories
            elfnumb += 1
            calories = 0
    maxcalelf = max(elfdict.items(), key=lambda x: x[1])
    return elfdict,  maxcalelf






toprint = caloriescounter("E:/PythonProjects/AdventOfCode/Day1Package/test.xlsx")
print(toprint[1])


