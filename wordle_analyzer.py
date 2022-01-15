# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 19:21:34 2022

@author: jared
"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

combinations = []
fiveLetterWords = []
lettersInWords = []
letterPos = {'First': [], 'Second' : [], 'Third': [], 'Fourth': [], 'Fifth': []}
def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def split(word):
    return [char for char in word]



def disPlot(letters):
    letters.sort()
    fig = sns.displot(data=letters, bins=26)
    plt.title("Letters most frequently used in five letter English words.")
    plt.xlabel("Letter")
    plt.ylabel("Number of occurences")
    plt.show()
    
    return fig

if __name__ == '__main__':
    english_words = load_words()
    # demo print
    for i in english_words:
        if len(i) == 5:
            fiveLetterWords.append(i)
            letters = split(i)
            letterPos['First'].append(i[0])
            letterPos['Second'].append(i[1])
            letterPos['Third'].append(i[2])
            letterPos['Fourth'].append(i[3])
            letterPos['Fifth'].append(i[4])
            combinations.append((i[0:2]))
            combinations.append((i[1:3]))
            combinations.append((i[2:4]))
            combinations.append((i[3:5]))
            
            for u in letters:
                lettersInWords.append(u)
                
    
    print(len(fiveLetterWords))   
    #position of letter frequency heatmap    
    posFrequency = {1: (Counter(letterPos['First'])),2: (Counter(letterPos['Second'])), 3: (Counter(letterPos['Third'])), 4: (Counter(letterPos['Fourth'])), 5: (Counter(letterPos['Fifth']))}
    posFreqDF = pd.DataFrame.from_dict(posFrequency, orient='index').reset_index()
    posFreqDF = posFreqDF[['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']]
    
    
    ax = plt.axes()
    plt.clf()
    sns.heatmap(posFreqDF, cmap="rocket_r", yticklabels = ['First', 'Second', 'Third', 'Fourth', 'Fifth']).set_title('Frequency of letters in each position of 15,918 five letter words')
    sns.set(rc = {'figure.figsize':(16,9)})
    plt.show()
    
    
    
    #frequency of individual letters
    oneLetterFrequency = (Counter(lettersInWords))
    olfDF = pd.DataFrame.from_dict(oneLetterFrequency, orient='index').reset_index()
    olfDF.rename({'index':'letter', 0:'count'}, axis=1, inplace=True)
    olfDF.sort_values(by=['count'], inplace=True)
    
    ax = plt.axes()
    plt.clf()
    
    sns.set_theme(style="whitegrid")
    sns.barplot(x = 'letter', y = 'count', data=olfDF).set_title('Frequency of letters apearing in 15,918 five letter words')
    sns.set(rc = {'figure.figsize':(16,9)})
    plt.xlabel("Letter")
    plt.ylabel("Number of occurences")
    plt.show()
    
    #frequency of pairs of letters
    twoLetterFrequency = (Counter(combinations))
    tlfDF = pd.DataFrame.from_dict(twoLetterFrequency, orient='index').reset_index()
    tlfDF.rename({'index':'letter', 0:'count'}, axis=1, inplace=True)
    tlfDF.sort_values(by=['count'], inplace=True)
    tlfDF = tlfDF[tlfDF['count'] >= 450]
    
    ax = plt.axes()
    plt.clf()
    
    sns.set_theme(style="whitegrid")
    sns.barplot(x = 'letter', y = 'count', data=tlfDF).set_title('Frequency of two letter combinations apearing in 15,918 five letter words')
    sns.set(rc = {'figure.figsize':(16,9)})
    plt.xlabel("Letter combination")
    plt.ylabel("Number of occurences")
    plt.show()
    
      
       
    print(posFreqDF)
    print(olfDF)
    print(tlfDF)           