# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 13:31:17 2018

@author: foxta
"""

#import nltk
import nltk
import csv

from nltk import word_tokenize

#open file
f = open('C:/Users/foxta/OneDrive - McGill University/GLIS 630/Final Project/Dataset/news_on_catalonia_oct_11_2017_LGMK.csv', 'r', encoding = "ISO-8859-1")

#define var for file
csv_f = csv.reader(f)

#define variable for list of words
listOfWordsES = "Soy un place-holder"

#loop through csv file to convert sentences to words
for rowES in csv_f:
    if rowES[5] == "Spanish":
        listOfWordsES = nltk.word_tokenize(rowES[7], "Spanish")
        print(listOfWordsES)