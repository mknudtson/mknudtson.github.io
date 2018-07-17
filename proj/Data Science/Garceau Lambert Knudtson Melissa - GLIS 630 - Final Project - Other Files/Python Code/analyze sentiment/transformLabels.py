# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 13:32:15 2018

@author: foxta
"""

#import nltk
import nltk
import csv

#open file
f = open('C:/Users/foxta/OneDrive - McGill University/GLIS 630/Final Project/Python code/sentimentAnalyzer/sentimentAnalyser_Vader/labelFloat.csv', 'r', encoding = "ISO-8859-1")

#define var for file
csv_f = csv.reader(f)

#loop through csv file to convert articles to sentences

print("IF YOU CAN READ THIS, EVERYTHING PRINTED")

for row in csv_f:
  if float(row[3]) > 0.5:
          print("5")
  elif float(row[3]) < -0.5:
          print("1")
  elif float(row[3]) > 0:
          print("4")
  elif float(row[3]) < 0:
          print("2")          
  else:
          print("3")
  
  #elif row[5] == "French":