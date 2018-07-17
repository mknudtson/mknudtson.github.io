# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 18:43:57 2018

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

from nltk.corpus import stopwords 

#define function
def cleanupDoc(s):
 #replace english with french, spanish or spanish (spanish works for catalan)
 stopset = set(stopwords.words('french'))
 tokens = nltk.word_tokenize(s)
 cleanup = [token.lower() for token in tokens if token.lower() not in stopset and  len(token)>2]
 return cleanup

#assign sentence to var to be used in function
#replace sentence below with text that needs stopwords removed
s = """Catalonia est bon oui"""

#assign function to var
x = cleanupDoc(s)
#if you can see "TOP" then output not truncated
#if output truncated then close console and open new console

#print function
print("\n TOP \n")
for word in x:
    print(word)