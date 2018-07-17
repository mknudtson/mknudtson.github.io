# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 13:32:15 2018

@author: foxta
"""

#import nltk
import nltk
import csv

#ACCURACY -- ALL

#open file
f = open('C:/Users/foxta/OneDrive - McGill University/GLIS 630/Final Project/Dataset/Back-up versions/2018032501 - Automatic labels/news_on_catalonia_oct_11_2017_LGMK.csv', 'r', encoding = "ISO-8859-1")

#define var for file
csv_f = csv.reader(f)

counter = 0

#skip first line of csv file
next(csv_f)
#now start looping through
for row in csv_f:  
  #check for any difference between the manual and the automatic label
  if int(row[8]) > 0:
      #set vars with correct types and intuitive names
      sent_manuInt = int(row[8])
      sent_autoInt = int(row[9])
      #where there is a difference between manual and automatic:
      if sent_manuInt > sent_autoInt:
          #if manual > automatic, find out what the difference is
          if (sent_manuInt - sent_autoInt) > 2:
              #if the difference exceeds +/-2, add 1 to counter
              counter = counter + 1
      elif sent_autoInt > sent_manuInt:
          #if automatic > manual, find out what the difference is
          if (sent_autoInt - sent_manuInt) > 2:
              #if the difference exceeds +/-2, add 1 the counter
              counter = counter + 1    
              
print("Number of automatically labelled records that are inaccurately labelled: " + str(counter))    
print("Percentage accuracy: " + str(((383 - counter) / 383) * 100))

#ACCURACY -- EN

#open file
f = open('C:/Users/foxta/OneDrive - McGill University/GLIS 630/Final Project/Dataset/Back-up versions/2018032501 - Automatic labels/news_on_catalonia_oct_11_2017_LGMK.csv', 'r', encoding = "ISO-8859-1")

#define var for file
csv_f = csv.reader(f)

counterEN = 0
counterRecordsEN = 0

#skip first line of csv file
next(csv_f)
#now start looping through
for row in csv_f:
    if row[5] == "English" and int(row[8]) > 0:
      #count records in EN
      counterRecordsEN  = counterRecordsEN + 1
      #check for any difference between the manual and the automatic label
      if int(row[8]) > 0:
          #set vars with correct types and intuitive names
          sent_manuInt = int(row[8])
          sent_autoInt = int(row[9])
          #where there is a difference between manual and automatic:
          if sent_manuInt > sent_autoInt:
              #if manual > automatic, find out what the difference is
              if (sent_manuInt - sent_autoInt) > 2:
                  #if the difference exceeds +/-2, add 1 to counter
                  counter = counter + 1
          elif sent_autoInt > sent_manuInt:
              #if automatic > manual, find out what the difference is
              if (sent_autoInt - sent_manuInt) > 2:
                  #if the difference exceeds +/-2, add 1 the counter
                  counterEN = counterEN + 1    
              
print("ENGLISH: Number of automatically labelled records that are inaccurately labelled: " + str(counterEN))    
print("ENGLISH: Percentage accuracy: " + str(((counterRecordsEN - counterEN) / counterRecordsEN) * 100))

#ACCURACY -- FR

#open file
f = open('C:/Users/foxta/OneDrive - McGill University/GLIS 630/Final Project/Dataset/Back-up versions/2018032501 - Automatic labels/news_on_catalonia_oct_11_2017_LGMK.csv', 'r', encoding = "ISO-8859-1")

#define var for file
csv_f = csv.reader(f)

counterFR = 0
counterRecordsFR = 0

#skip first line of csv file
next(csv_f)
#now start looping through
for row in csv_f:
    if row[5] == "French" and int(row[8]) > 0:
      #count records in FR
      counterRecordsFR  = counterRecordsFR + 1
      #check for any difference between the manual and the automatic label
      if int(row[8]) > 0:
          #set vars with correct types and intuitive names
          sent_manuInt = int(row[8])
          sent_autoInt = int(row[9])
          #where there is a difference between manual and automatic:
          if sent_manuInt > sent_autoInt:
              #if manual > automatic, find out what the difference is
              if (sent_manuInt - sent_autoInt) > 2:
                  #if the difference exceeds +/-2, add 1 to counter
                  counterFR = counterFR + 1
          elif sent_autoInt > sent_manuInt:
              #if automatic > manual, find out what the difference is
              if (sent_autoInt - sent_manuInt) > 2:
                  #if the difference exceeds +/-2, add 1 the counter
                  counterFR = counterFR + 1    
              
print("FRENCH: Number of automatically labelled records that are inaccurately labelled: " + str(counterFR))    
print("FRENCH: Percentage accuracy: " + str(((counterRecordsFR - counterFR) / counterRecordsFR) * 100))

#ACCURACY -- ES

#open file
f = open('C:/Users/foxta/OneDrive - McGill University/GLIS 630/Final Project/Dataset/Back-up versions/2018032501 - Automatic labels/news_on_catalonia_oct_11_2017_LGMK.csv', 'r', encoding = "ISO-8859-1")

#define var for file
csv_f = csv.reader(f)

counterES = 0
counterRecordsES = 0

#skip first line of csv file
next(csv_f)
#now start looping through
for row in csv_f:
    if row[5] == "Spanish" and int(row[8]) > 0:
      #count records in ES
      counterRecordsES  = counterRecordsES + 1
      #check for any difference between the manual and the automatic label
      if int(row[8]) > 0:
          #set vars with correct types and intuitive names
          sent_manuInt = int(row[8])
          sent_autoInt = int(row[9])
          #where there is a difference between manual and automatic:
          if sent_manuInt > sent_autoInt:
              #if manual > automatic, find out what the difference is
              if (sent_manuInt - sent_autoInt) > 2:
                  #if the difference exceeds +/-2, add 1 to counter
                  counterES = counterES + 1
          elif sent_autoInt > sent_manuInt:
              #if automatic > manual, find out what the difference is
              if (sent_autoInt - sent_manuInt) > 2:
                  #if the difference exceeds +/-2, add 1 the counter
                  counterES = counterES + 1    
              
print("SPANISH: Number of automatically labelled records that are inaccurately labelled: " + str(counterES))    
print("SPANISH: Percentage accuracy: " + str(((counterRecordsES - counterES) / counterRecordsES) * 100))

#ACCURACY -- CA

#open file
f = open('C:/Users/foxta/OneDrive - McGill University/GLIS 630/Final Project/Dataset/Back-up versions/2018032501 - Automatic labels/news_on_catalonia_oct_11_2017_LGMK.csv', 'r', encoding = "ISO-8859-1")

#define var for file
csv_f = csv.reader(f)

counterCA = 0
counterRecordsCA = 0

#skip first line of csv file
next(csv_f)
#now start looping through
for row in csv_f:
    if row[5] == "Catalan" and int(row[8]) > 0:
      #count records in CA
      counterRecordsCA  = counterRecordsCA + 1
      #check for any difference between the manual and the automatic label
      if int(row[8]) > 0:
          #set vars with correct types and intuitive names
          sent_manuInt = int(row[8])
          sent_autoInt = int(row[9])
          #where there is a difference between manual and automatic:
          if sent_manuInt > sent_autoInt:
              #if manual > automatic, find out what the difference is
              if (sent_manuInt - sent_autoInt) > 2:
                  #if the difference exceeds +/-2, add 1 to counter
                  counterCA = counterCA + 1
          elif sent_autoInt > sent_manuInt:
              #if automatic > manual, find out what the difference is
              if (sent_autoInt - sent_manuInt) > 2:
                  #if the difference exceeds +/-2, add 1 the counter
                  counterCA = counterCA + 1    
              
print("CATALAN: Number of automatically labelled records that are inaccurately labelled: " + str(counterCA))    
print("CATALAN: Percentage accuracy: " + str(((counterRecordsCA - counterCA) / counterRecordsCA) * 100))