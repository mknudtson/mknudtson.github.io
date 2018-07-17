# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 22:08:54 2018

@author: foxta
"""

import nltk

#prepare text for use with nltk lexical dispersion plot feature
f = open('C:/Users/foxta/OneDrive - McGill University/GLIS 630/Final Project/Dataset/news_on_catalonia_oct_11_2017_LGMK.csv', 'r', encoding = "ISO-8859-1")
raw = f.read()
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)

#testing overall dispersion plots
#text.dispersion_plot(["illegal", "unilateral", "secession", "Franco"])
#text.dispersion_plot(["doute", "loi", "problème", "juridique"])

#
 
import csv
   
#prepare csv file for use with nltk lexical dispersion plot feature
d = open('C:/Users/foxta/OneDrive - McGill University/GLIS 630/Final Project/Dataset/news_on_catalonia_oct_11_2017_LGMK_sort.csv', 'r', encoding = "ISO-8859-1")
csv_d = csv.reader(d)

#create vars corresponding to empty strings to store text by langauge
textEN = ""
textFR = ""
textES = ""
textCA = ""

for row in csv_d:
    if row[5] == "English":
        textEN = textEN + row[7]
    elif row[5] == "French" and int(row[6]) < 13:
        textFR = textFR + row[7]
    #ADD elif for ES
    #ADD else for CA
tokensEN = nltk.word_tokenize(textEN)
textENForLDP = nltk.Text(tokensEN)
tokensFR = nltk.word_tokenize(textFR)
textFRForLDP = nltk.Text(tokensFR)
#ADD same for ES
#ADD same for CA

#EN only LDP - use most popular words from word cloud
textENForLDP.dispersion_plot(["government", "Rajoy", "Puigdemont", "illegal", "separatist"])

#FR only LDP - use most popular words from word cloud
textFRForLDP.dispersion_plot(["gouvernement", "Rajoy", "Puigdemont", "illégal", "séparatiste"])

#ADD ES only LDP - most pop. words from word cloud
#ADD CA only LDP - most pop. words from word cloud