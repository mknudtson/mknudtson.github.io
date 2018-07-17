# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 13:32:15 2018

@author: foxta
"""

#import nltk
import nltk
import csv

#open file
f = open('C:/Users/foxta/OneDrive - McGill University/GLIS 630/Final Project/Dataset/news_on_catalonia_oct_11_2017_LGMK.csv', 'r', encoding = "ISO-8859-1")

#define var for file
csv_f = csv.reader(f)

#skip first line of csv file
next(csv_f)
#now start looping through
print("SIMPLIFIED SENTIMENT")
for row in csv_f:  
  sent_autoInt = int(row[9])
  if sent_autoInt == 1:
      print("1")
  elif sent_autoInt == 2:
      print("1")
  elif sent_autoInt == 3:
      print("2")
  elif sent_autoInt == 4:
      print("3")
  elif sent_autoInt == 4:
      print("3")      