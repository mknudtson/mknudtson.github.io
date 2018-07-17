# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 10:25:53 2018

@author: foxta
"""

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import csv

#open file
f = open('C:/Users/foxta/OneDrive - McGill University/GLIS 630/Final Project/Dataset/news_on_catalonia_oct_11_2017_LGMK.csv', 'r', encoding = "ISO-8859-1")

#define var for file
csv_f = csv.reader(f)
  
sid = SentimentIntensityAnalyzer()

print("I HOPE THIS WORKS")

for row in csv_f:
     #print(sentence)
     ss = sid.polarity_scores(row[7])
     for k in ss:
         print('{0}: {1}, '.format(k, ss[k]), end='')
     print()