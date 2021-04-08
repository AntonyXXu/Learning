# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 16:12:13 2020

@author: Test
"""
#%%
f=open("myfile.txt","w")
print(type(f))
f.write("\n hello! \n hello \n world \n")
f.close()

#%%
f=open("myfile.txt","r")
print(type(f))
data=f.read()
print(data)
f.close()

#%%
with open("myfile.txt","r") as f:
    data=f.read()
    print(data)
    