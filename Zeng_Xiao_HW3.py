# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:10:55 2016
Homework 3
@author: Xiao Zeng
"""

import pandas as pd              #Used to generate dataframes
import matplotlib.pyplot as plt  #Used to draw graphs


#Question 1
"""Creating a Datafrrame type and adding column names using the 'read_csv' method. """    

url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'        #Input the link         
                    
df = pd.read_csv(url, names=['Sepal Length','Sepal Width', 'Petal Length','Petal Width','Class'])  #Converts the data to a dataframe type and adds column names

#Question 2
print(df.head(10))  #Prints the first 10 rows of the dataframe
print(df.tail(10))  #Prints the last 10 rows of the dataframe


#Question 3
"""Displaying simple location statistics (Count, Mean, STD, Min, 25%, 50%, 75%, MAX)"""
print(df.describe()) #Prints various statistics

#Question 4
def print_plot(binsizes):
   """This fucntion prints plots for each numeric columns with different input bin sizes.
       
   Parameters: A list of numbers, representing different bin sizes
   Returns: None, but the function will print several graphs.
       
   """
   cnames=['Sepal Length','Sepal Width', 'Petal Length','Petal Width']
   for c in cnames:
       for sizes in binsizes: #For every bin size, prints the graphs for each numeric columns
     
          plt.figure(); #Drawing graphs
          df.hist(column = c, bins=sizes)  #This method automatically prints the histograms for numeric columns

   
   return None

print_plot([10,50,100])  

#Question 5
"""Plotting a box plot for each of the numeric column."""
plt.figure()
df.boxplot()    #This method prints the box plots for each column and displays them in one graph.
     
     
     
#Question 6
"""Plotting a bar chart for the nominal column."""
df.Class.value_counts().plot(kind='bar') 
#.Class selects the 'Class' column. and .value_counts() counts how many times a string appears in the column. Then put all the counted strings into a bar chart
     
     
     
