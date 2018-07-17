# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 13:31:17 2018

@author: foxta
"""

#import nltk
import nltk
import csv

#open file
f = open('C:/Users/foxta/OneDrive - McGill University/GLIS 630/Final Project/Dataset/news_on_catalonia_oct_11_2017_LGMK.csv', 'r', encoding = "ISO-8859-1")

#define var for file
csv_f = csv.reader(f)

#(ONE-TIME) download nltk punkt sentence tokenizer
#nltk.download('punkt')

#test punkt sentence tokenizer
testingTesting = nltk.sent_tokenize("""L'Exposició Internacional de Barcelona tingué lloc del 20 de maig de 1929 al 15 de gener de 1930 a Barcelona. Se celebrà a la muntanya de Montjuïc, on ocupà una superfície de 118 hectàrees, i tingué un cost de 130 milions de pessetes. Entre la vintena de nacions europees que hi participaren hi havia països com Alemanya, Bèlgica, Dinamarca, França, Hongria, Itàlia, Noruega, Romania o Suïssa. També hi van prendre part expositors privats japonesos i nord-americans.""", "Spanish")
print(testingTesting)

#(ONE-TIME) download nltk stopwords
#nltk.download('stopwords')

#test nltk stopwords (english, spanish and french - catalan not available)
print(nltk.corpus.stopwords.words('english'))
print(nltk.corpus.stopwords.words('french'))
print(nltk.corpus.stopwords.words('spanish'))

#define variable for list of sentences
listOfSentences = "place-holder"

#loop through csv file to convert articles to sentences
for row in csv_f:
  if row[5] == "English":
          listOfSentences = nltk.sent_tokenize(row[7], "English")
  elif row[5] == "French":
          listOfSentences = nltk.sent_tokenize(row[7], "French")
  elif row[5] in ("Spanish", "Catalan"):
          listOfSentences = nltk.sent_tokenize(row[7], "Spanish")
  print('\n')
  print("ARTICLE NUMBER " + str(row[0]) + " (total number of sentences: " + str(len(listOfSentences)) + ")")
  for i in listOfSentences:
      print(i)