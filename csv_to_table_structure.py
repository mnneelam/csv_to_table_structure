
# coding: utf-8

# In[1]:

#A program that reads in a csv file and tries to take a guess at what could be the possible table structure, 
#columns and many other properties
#1) How many rows?
#2) How many columns?
# 3) Are there any rows in error where columns don't match (mismatched column count), group rows by number of columns present 
# and assume most frequently occuring number of rows is the right number, everything else is error rows, to be ignored or reported
# 4) Eliminate error rows
# 5) get the primary key column based on uniqueness of the values (cardinality of each column)
#6) Count of Null values in each column
#7) Cardinality of each column


# In[2]:

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import sys

# In[3]:

if len(sys.argv) == 1:
 print "You can also give filename as command line argument"
 filename = raw_input("Enter Filename:")
 print "filename specified is: "+filename
else:
 filename = sys.argv[1]

#filename = input('Enter File name (full path):')
dframe = pd.read_csv(filename,sep=',')
#dframe


# In[4]:

dframe.dtypes


# In[5]:

dframe.columns


# In[6]:

dframe.describe()


# In[7]:

#how to get columns
columns = len(dframe.columns)
text_file = open("csv_to_table1.txt", "w")
text_file.write("Number of columns: %d\n" %columns)
columns


# In[8]:

#how to get number of rows
rows = len(dframe.index)
text_file.write("Number of rows: %s\n" %rows)
rows


# In[9]:

#group rows by columns
dframe.shape[0]


# In[10]:

dframe.count()


# In[11]:

text_file.write("Column and rows: %s\n" %dframe.isnull().sum())
#get count of null values in each column (Most efficient for large files)
dframe.isnull().sum()


# In[12]:

#alternate way to get count of null values in each column
count_nan = len(dframe) - dframe.count()
count_nan


# In[13]:

#Find rows who has null column values
dframe.isnull().any(axis=1)


# In[14]:

#now select rows which have null column values
dframe[dframe.isnull().any(axis=1)]


# In[15]:

#how to find unique values for columns
data_column = {}
possible_index_col_name=[]
for col in dframe:
    data_column[col] = dframe[col].unique()
  
#dframe[col].where(data_column[col].count == len(dframe.index()))
#list(dframe)
data_column
#possible_index_col = data_column.count()
#possible_index_col
#dframe.columns.values


# In[16]:

len_unique=0
for i in data_column:
    unique, counts = np.unique(data_column[i], return_counts=True); len_unique=len(unique);
    print "column name "+i+" has "+str(len_unique)+" unique elements, cardinality is "+str(float(len_unique)/rows)
    text_file.write("column name  "+i+" has "+str(len_unique)+" unique elements, cardinality is "+str(float(len_unique)/rows)+"\n")


# In[ ]:




# In[17]:

#data_column is a dictionary with unique values for columns
# divide data_column with number of rows to get the cardinality of columns
# if the answer is 1, it is likely to be an index column, print it's name
text_file.write("index columns: ")
index1=0
for i in data_column:
    if len(data_column[i])/rows == 1:
        print i; print '\n'; index1+=1; text_file.write("index column: %d is" %index1); text_file.write("  %s\n" %i)


# In[18]:

null_val_data = {}
#count the number of null values in each column
null_val_data = dframe.isnull().sum()
len(null_val_data)
null_val_data
#if cmp(null_val_data,0):
#for i in null_val_data:
 #   if null_val_data[i] > 0:            print null_val_data[i]
    #if !cmp(null_val_data,0)
        


# In[19]:

text_file.close()

