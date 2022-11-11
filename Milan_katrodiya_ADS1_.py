# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:36:51 2022

@author: Admin
"""

# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt



"""
LINE PLT
"""

# Read csv file 
abnb = pd.read_csv('ABNB.csv') 
print(abnb)

# Plotting multiple lines graph
plt.figure(figsize=(9,9))
plt.plot(abnb["Open"], label="Open")
plt.plot(abnb["High"], label="High")
plt.plot(abnb["Low"], label="Low")
plt.plot(abnb["Close"], label="Close")
plt.legend()
plt.xlabel("Data")
plt.ylabel("Volumes")
plt.show()



"""
  HISTOGRAM PLT
"""

# Read csv file
score = pd.read_csv('adm_data.csv')
print(score)

# Plotting 2 histograms with features
plt.figure(figsize=(8,8))
plt.hist(score["CGPA"], label="CGPA",bins=4)
plt.hist(score["SOP"], label="SOP",bins=4)
plt.legend()
plt.xlabel("Grades")
plt.ylabel("Frequency")
plt.show()



"""
PIE PLT
"""

# Read csv file
country = pd.read_csv('ghi.csv')
print(country)

names = ["Afghanistan", "Albania", "Bangladesh", "Bolivia", "Bosnia and Herzegovina"]

plt.figure()
plt.pie(country["Global Hunger Index (2021)"], labels=names, autopct='%1.1f%%')
plt.title("Golbal Hunger Index")
plt.show()
