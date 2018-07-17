# -*- coding: utf-8 -*-

from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
#import nltk
    
d = path.dirname(__file__)


# Read the whole text.
text = open(path.join(d, 'english.txt')).read()

stopwords = set(STOPWORDS)
stopwords.add("said")

wordcloud = WordCloud(width=1600, height=800).generate(text)
# Open a plot of the generated image.

plt.figure( figsize=(20,10), facecolor='k')
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()