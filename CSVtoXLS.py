# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 12:46:43 2017

@author: skiter
"""

import os
import pandas as pd
writer = pd.ExcelWriter('output.xlsx')
path=os.getcwd() + '\\csv'
os.chdir(path)
path=os.getcwd()
print('current dir: ', path)
row = 0
for path,dirs,files in os.walk(path):
    print(files)
    print('=========')
    for file in files:
        print(file)
        df = pd.read_csv(file)
        print("number of rows: ", df.shape[0])
        df['Timestamp'] = pd.to_datetime(df['Timestamp'], dayfirst=True)
        #print("INTSYNC#", df.iloc[:,0].str.contains("INTSYNC").count())
        #print((df.iloc[:,0].str.contains("INTSYNC")[df.iloc[:,0].str.contains("INTSYNC")==True]).index)
        df.drop((df.iloc[:,0].str.contains("INTSYNC")[df.iloc[:,0].str.contains("INTSYNC")==True]).index, inplace=True)
        #print("INTSYNC#", df.iloc[:,0].str.contains("INTSYNC").count())
        df.to_excel(writer, sheet_name="Data", index=False, startrow=row)
        row += df.shape[0] + 2
        del df
        
        
writer.save()
print ("DONE!")