from textblob import TextBlob
from codecs import *
from nltk import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import codecs
import csv

def sentiment(message):
    blob = TextBlob(message)
    if blob.sentiment.polarity > 0 :
        return 'Positive'
    elif blob.sentiment.polarity < 0 :
        return 'Negative'
    else:
        return 'Neutral'

def removeLink(message):
    x=re.sub("(https://[^ ]+)", "", message)
    return x

def removeAt(message):
    x = re.sub(r'(\s)@\w+', r'\1', message)
    return x

def removeHash(message):
    x = re.sub(r'#(\w+)', r'\1', message)
    return x

#csv file reading
def csvReader():
    with open('tweets_Shobhit.csv','rb', encoding="utf8") as tweetCSV:
        csvFile = csv.reader(tweetCSV)
        for row in csvFile:
            x = sentiment(removeHash(removeAt(removeLink(row[1]))))
            with open('tweets_sentiment1.csv', 'a', encoding="utf8") as tweetCSV1:
                csvFileWrite = csv.writer(tweetCSV1,delimiter = ',')
                csvFileWrite.writerow((row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],x))

csvReader()