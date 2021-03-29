# import things
from textblob import TextBlob
from pathlib import Path
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import pandas as pd
from textblob import Word
from operator import itemgetter
 
# Create object to hold stop words
stops = stopwords.words("english")
 
# create a list that contains the book of john stop words
Book_of_John_Stop_Words = [
    "thy",
    "ye",
    "verily",
    "thee",
    "hath",
    "say",
    "thou",
    "art",
    "shall",
    "saith",
]
 
# add in the book of john stop words
stops += Book_of_John_Stop_Words
 
# read the book of john text
text = Path("book of John text.txt").read_text()
 
# Tokenize the words
tokens = nltk.word_tokenize(text)
 
# Create a list of tuples that contain the word and its tag
tags = nltk.pos_tag(tokens)
 
# Filter out nouns
nouns = [
    word
    for word, pos in tags
    if (pos == "NN" or pos == "NNP" or pos == "NNS" or pos == "NNPS")
]
 
# Convert to text of nouns
noun_text = " ".join(nouns).lower()
 
# Turn noun text into a blob
noun_blob = TextBlob(noun_text)
 
# Count the items in the blob
items = noun_blob.word_counts.items()
 
# Filter out the stops
items_no_stops = [item for item in items if item[0] not in stops]
 
# Sort the items by their count
sorted_items = sorted(items_no_stops, key=itemgetter(1), reverse=True)
 
# Store top 15 in top15 variable
top15 = sorted_items[:15]
 
# Create a list to hold the words
words123 = []
 
# Append into words123 just the words
for x, y in top15:
    words123.append(x)
 
# Turn the words into text
text123 = " ".join(words123)
 
# generate wordcloud, send it to the bookofjohnwordcloud file
wordcloud = WordCloud(colormap="prism", background_color="white")
 
wordcloud = wordcloud.generate(text123)
 
wordcloud = wordcloud.to_file("BookOfJohnWordCloud.png")