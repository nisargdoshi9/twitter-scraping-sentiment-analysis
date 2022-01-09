# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 01:02:07 2022

@author: Nisarg's PC
"""
import re
import pandas as pd
data = pd.read_csv("melb_data.csv")
first = data["Unique ID"]

#ind =   re.findall(r'\d+', first[2])

ind=[]                                          #Initializing the new index list
for i in first:                                 #Splitting and extracting numbers in int format
    temp_str = i.split("_")
    ind.append(int(temp_str[1]))

    #print(i)
    #ind = [int(s) for s in i.split() if s.isdigit()]
    #ind = [int(x) for x in i.split() if x.isdigit()]
    #ind = [int(s) for s in re.findall(r'\b\d+\b', i)]
#print(ind)

data_new = pd.read_csv("melb_data.csv")         #Creating a new data frame for demo
data_new['New_Index']=ind                       #Assigning a new column tom data frame with new index

#data_new['New_Index'] = data_new['New_Index'].astype(str).astype(int)
#print(data_new["New_Index"])
#data_new.index = list(data_new[""])
#data_new.reindex(ind) #Reindexeing data frame to ind (New_Index)
#index1 = pd.Index(ind)                         #Didn't work
#data_new = data_new.set_index(ind)
print(data_new)                                 #Printing data frame with old index
data_new = data_new.set_index('New_Index')
print(data_new)                                 #Printing data frame with new index
#print(data_new.dtypes)
#print("\n",data_new)
