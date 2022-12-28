# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 05:28:05 2022

@author: Nisarg's PC
"""
# =============================================================================
# Load the data using Pandas
# =============================================================================
import pandas as pd
import numpy as np
df=pd.read_csv(r"C:\{My Drive}\ML\WoC\Eval\archive\tripadvisor_hotel_reviews.csv")


# =============================================================================
# We’ll be detecting 3 basic sentiments in the text provided in the review i.e. positive, neutral and negative.
# Convert ‘Rating’ column of the dataframe to 0s (negative), 1s (neutral) and 2s (positive) according to the following criteria:
# 1-2 -> 0
# 3   -> 1
# 4-5 -> 2
# 
# 
# =============================================================================
values=[]
for i in range(0,len(df['Rating'])):
    values.insert(i,(df['Rating'][i]))

df['New Rating']=values

for i in range(0,len(df['Rating'])):
    if(values[i]<3):
        df['New Rating'][i]=0
    elif(values[i]==3):
        df['New Rating'][i]=1
    else:
        df['New Rating'][i]=2

# =============================================================================
# Deal with any missing values, incorrect domain values in any way you may want to
# =============================================================================
x=df.isnull()
flag=0
for i in range(0,len(x['Rating'])):
    if(x['Rating'][i]==True):
        flag=1
print(flag)



# =============================================================================
# Lower all the text.
# =============================================================================
df.Review=[i.lower() for i in df.Review]

# =============================================================================
# Remove all the hyperlinks if present in the text.
# =============================================================================

import re
for i in range(0,len(df['Review'])):
  df['Review'][i] = re.sub(r'^https?:\/\/.*[\r\n]*', '', df['Review'][i], flags=re.MULTILINE)
df['Review'] = df['Review'].apply(lambda x: re.split('www.*', str(x))[0])
    
# =============================================================================
# t = df.copy(deep=True)
# for i in range(0,len(t['Review'])):
#   t['Review'][i] = re.sub(r'[^a-zA-Z\s:]', ' ', t['Review'][i], flags=re.MULTILINE)
# 
# =============================================================================


# =============================================================================
# Substitute all the non alphabetical characters(a-z) by ‘ ‘ (space).
# =============================================================================

for i in range(0,len(df['Review'])):
  df['Review'][i] = re.sub(r'[^a-zA-Z\s:]', ' ', df['Review'][i], flags=re.MULTILINE)

# =============================================================================
# If there are multiple consequent spaces in the text, replace them by a single space (for example ‘    ‘ to ‘ ‘ ).
# =============================================================================

for i in range(0,len(df['Review'])):
  df['Review'][i]=" ".join(df['Review'][i].split())
  
  
# =============================================================================
# Tokenize all the Review strings.
# =============================================================================
import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize
df['Tokenized_Review']=[0 for x in df['Review']]
for i in range(0,len(df.Tokenized_Review)):
    df.Tokenized_Review[i]=word_tokenize(df.Review[i]) 


# =============================================================================
# Remove all the tokens which are English stopwords ( You can use nltk.corpus).
# =============================================================================
nltk.download('stopwords')
from nltk.corpus import stopwords

stop_words=set(stopwords.words('english'))
df['After_Stopwords_Removal']=[[] for x in df.Review]

l=df.shape[0]
for i in range(0,l):
    for j in range(0,len(df.Tokenized_Review[i])):
        if df.Tokenized_Review[i][j] not in stop_words:
            df['After_Stopwords_Removal'][i].append(df.Tokenized_Review[i][j])

# =============================================================================
# Stem all the words using PorterStemmer.        
# =============================================================================
from nltk.stem import PorterStemmer
ps=PorterStemmer()
df['Stemmed'] = [[] for x in df.Review]
for i in range(0,len(df['After_Stopwords_Removal'])):
    for w in df.After_Stopwords_Removal[i]:
        df['Stemmed'][i].append(ps.stem(w))
