# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 17:00:52 2020

@author: Test
"""

import csv
with open("simpledata.csv","r") as f:
    reader=csv.reader(f)
    for row in reader:
        print(type(row))
        print(row)
        
#%%
d = []
with open("simpledata.csv", "r") as f:
    reader = csv.reader(f)
    row_num = 0
    for row in reader:
        if row_num == 0:
            d.append(row)
        else:
            d.append([row[0].upper(),row[1]])
        row_num += 1
print(d)

#%%
with open("simpledata2.csv", "w") as f:
    writer = csv.writer(f)
    for row in d:
        writer.writerow(row)
        
#%%
with open("simpledata2.csv","r") as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)