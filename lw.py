import random
import string
import os
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import math

import urllib.request
#url = 'http://www.gutenberg.org/cache/epub/514/pg514.txt'
#response = urllib.request.urlopen(url)
#data = response.read()  # a `bytes` object
# text = data.decode('utf-8')
# print(text)  for testing

# I used txt files instead of pulling from internet ( but showed code on how to do this) because I was working on this on a train when I had not internet


def process_file(filename, skip_header):
    """
    Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header

    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding='utf8')

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break
        line = line.replace('-', ' ')
        strippables = string.punctuation + string.whitespace

        for word in line.split():
            # remove punctuation and convert to lowercase
            word = word.strip(strippables)
            word = word.lower()

            # update the histogram
            hist[word] = hist.get(word, 0) + 1

    return hist


def skip_gutenberg_header(fp):
    """
    Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS PROJECT'):
            break

def most_common(hist):
    """Makes a list of word-freq pairs(tuples) in descending order of frequency.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """
    t = []
    for key, value in hist.items():
        t.append((value, key))

    t.sort()
    t.reverse()
    return t


def print_most_common(hist, num=10):
    """
    Prints the most commons words in  histogram and their frequency

    hist: histogram--map from word to frequency
    num: number words to print
    """
    t = most_common(hist)
    for freq, word in t[:num]:
        print(word, '\t', freq)


def compare(hist, lovewords):
    """
    If word in book matches word in book, keep that word.

    book, lovewords: dictionaries
    """
    new = {}
    # hist = most_common(hist)
    for key in lovewords:
        if key in hist:
            new[key] = hist.get(key, 0)
    return new

#ANALYSIS

lovewords = process_file('lovewords.txt', skip_header=False)
book = process_file('bronte1.txt', skip_header=True)

def bronte1():
    hist = process_file('bronte1.txt', skip_header=True)
    lovewords = list(process_file('lovewords.txt', skip_header=False).keys())
    t = compare(hist, lovewords)
    #print('The most common love words are:' )
    print_most_common(t ,num = 5)
    score1 = sum(hist.values())
    return score1

def bronte2():
    hist = process_file('bronte2.txt', skip_header=True)
    lovewords = list(process_file('lovewords.txt', skip_header=False).keys())
    t = compare(hist,lovewords)
    #print('The most common love words are:' )
    print_most_common(t ,num = 5)
    score2 = sum(hist.values())
    return score2

def bronte3():
    hist = process_file('bronte3.txt', skip_header=True)
    lovewords = list(process_file('lovewords.txt', skip_header=False).keys())
    t = compare(hist,lovewords)
    #print('The most common love words are:' )
    print_most_common(t ,num = 5)
    score3 = sum(hist.values())
    return score3

def bronte():
    score1 = int(bronte1())
    score2 = int(bronte2())
    score3 = int(bronte3())
    scoreBronte = (score1 + score2 + score3)/3
    print('lovescore for the Bronte sisters is: ')
    print(scoreBronte)
    print('................')
    return scoreBronte

def shake1():
    hist = process_file('shake1.txt', skip_header=True)
    lovewords = list(process_file('lovewords.txt', skip_header=False).keys())
    t = compare(hist,lovewords)
    print('The most common love words are:' )
    print_most_common(t ,num = 5)
    score4 = sum(hist.values())
    return score4

def shake2():
    hist = process_file('shake2.txt', skip_header=True)
    lovewords = list(process_file('lovewords.txt', skip_header=False).keys())
    t = compare(hist,lovewords)
    print('The most common love words are:' )
    print_most_common(t ,num = 5)
    score5 = sum(hist.values())
    return score5
    

def shake():
    score4 = int(shake1())
    score5 = int(shake2())
    scoreShake = (score4 +  score5)/2
    print('lovescore for Shakespeare is: ')
    print(scoreShake)
    print('.......................')
    return scoreShake

def austen():
    hist = process_file('austen1.txt', skip_header=True)
    lovewords = list(process_file('lovewords.txt', skip_header=False).keys())
    t = compare(hist,lovewords)
    print('The most common love words are:' )
    print_most_common(t ,num = 5)
    scoreAusten = sum(hist.values())
    print('lovescore for Jane Austen is: ')
    print(scoreAusten)
    print('...................')
    return scoreAusten

def plato():
    hist = process_file('plato.txt', skip_header=True)
    lovewords = list(process_file('lovewords.txt', skip_header=False).keys())
    t = compare(hist,lovewords)
    print('The most common love words are:' )
    print_most_common(t ,num = 5)
    scorePlato = sum(hist.values())
    print('lovescore for Plato is: ')
    print(scorePlato)
    print('...................')
    return scorePlato

#def sentiment_analysis(filename):
 #   score = SentimentIntensityAnalyzer().polarity_scores(filename)
    #return the polarity score of the text
  #  return score
#def cosine_similarity(filename, filename):

# I was not able to get nltk to give me results without error so that is why it is commented out, but I wanted to show that I did try it and play around with it for a while.
def bestloveauthor():
    #print("Sentiment analysis results of Plato:")
    #print(sentiment_analysis('plato.txt'))
    #print("Sentiment analysis results of Bronte:")
    #print(sentiment_analysis('bronte1.txt'))
    #print("Sentiment analysis results of Shakepeare:")
    #print(sentiment_analysis('shake1.txt'))
    #print("Sentiment analysis results of Austen:")
    #print(sentiment_analysis('austen1.txt'))
    print('Because I love romance books I wanted to find out which author has the most romance in their book/s!')
    print('To do this we give each author a lovescore:')
    scoreB = int(bronte())
    scoreS = int(shake())
    scoreA = int(austen())
    scoreP = int(plato())
    maximum = max('scoreB','scoreS', 'scoreA', 'scoreP')
    print('.....................')
    print('Since we now know the love score for each writer')
    print('Who writes the most about love?')
    print('.....................')
    print('Python says it is.... ')
    print(maximum)
    print('is the highest lovescore')
    print('This means Shakespeare wins!')

if __name__ == '__main__': 
    bestloveauthor()

    