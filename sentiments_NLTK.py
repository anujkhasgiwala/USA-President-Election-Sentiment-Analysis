import nltk
from codecs import *
from nltk import *
from nltk.corpus import stopwords
import codecs
import pickle
import csv

def tokenizeTweets(line):
    words1 = []
    stop = stopwords.words('english')
    stemmer = PorterStemmer()
    tokenizer = RegexpTokenizer('\w+')
    for word in tokenizer.tokenize(line):
        if word not in stop:
            # try:
            x=stemmer.stem(word).encode('utf-8',errors='strict')
            words1.append(x)
    return words1

def sentimentLabel(message):
    picklefile = open("bayes.pickle","rb")
    classifier = pickle.load(picklefile,fix_imports=True, encoding="utf-8", errors="strict")
    picklefile.close()
    label = classifier.classify(tokenizeTweets(message))
    #apply feature
    return label

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
    with open('tweets.csv','rb', encoding="utf8") as tweetCSV:
        csvFile = csv.reader(tweetCSV)
        for row in csvFile:
            print(sentimentLabel(removeHash(removeAt(removeLink(row[1])))))

csvReader()