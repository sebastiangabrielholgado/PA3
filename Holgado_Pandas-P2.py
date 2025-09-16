#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Problem#2: Use subsetting, slicing and indexing operations to extract data from the provided data

#access the pandas library
import pandas as pd

#Get the data from the cars.csv
df = pd.read_csv("cars.csv")

# a) Display the first five rows with odd-numbered columns 
#use an .iloc feature which lets me set ranges that are positioned based
df.iloc[0:5,[1,3,5,7,9,11]]

# b) Display the row that contains the ‘Model’ of ‘Mazda RX4’.
# use an .iloc again since I prefer using position based 
# this can be read as [row 0:row1,all columns]
df.iloc[0:1,:]

# c) How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
#use loc to vary using loc and iloc
# can be read as [row number,"column name"]
df.loc [23,"cyl"]

# d) Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

df.loc[[1,28,18],["Model","cyl","gear"]]


# In[ ]:




