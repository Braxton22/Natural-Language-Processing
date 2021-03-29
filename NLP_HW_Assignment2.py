from textblob import TextBlob
from pathlib import Path
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import pandas as pd
from textblob import Word
from operator import itemgetter
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

porter = PorterStemmer()
wnl = WordNetLemmatizer()

stops = stopwords.words("english")
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
]
for word in Book_of_John_Stop_Words:
    stops.append(word)

text = Path("book of John text.txt").read_text()

tokens = nltk.word_tokenize(text)
tags = nltk.pos_tag(tokens)
nouns = [
    word
    for word, pos in tags
    if (pos == "NN" or pos == "NNP" or pos == "NNS" or pos == "NNPS")
]

noun_text = " ".join(nouns).lower()

noun_blob = TextBlob(noun_text)

list_of_nouns = []

for word in noun_blob.words:
    list_of_nouns.append(word)

Formatted_nouns = []
for word in list_of_nouns:
    porter.stem(word)
    wnl.lemmatize(word)
    Formatted_nouns.append(word)

formatted_text = " ".join(Formatted_nouns)

formatted_text_blob = TextBlob(formatted_text)

items = formatted_text_blob.word_counts.items()

items = [item for item in items if item[0] not in stops]

sorted_items = sorted(items, key=itemgetter(1), reverse=True)

top15 = sorted_items[1:16]

print(top15)

words123 = []

for x, y in top15:
    words123.append(x)

text123 = " ".join(words123)

wordcloud = WordCloud(colormap="prism", background_color="white")

wordcloud = wordcloud.generate(text123)

wordcloud = wordcloud.to_file("BookOfJohnWordCloud.png")