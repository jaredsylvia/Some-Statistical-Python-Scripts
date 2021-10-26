# -*- coding: utf-8 -*-
"""
Created on Tue May  4 20:55:28 2021

@author: jared
"""

import json
import re
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import random

stopwords = set(STOPWORDS)

stopwords.add('Facebook') #Words you want removed from your wordclouds
stopwords.add('Trump')

postsFile = open('posts.json') #JSON files obtained through requesting copies of your data from Facebook.
commentsFile = open('comments.json')
groupsFile = open('groups.json')

posts = json.load(postsFile)
comments = json.load(commentsFile)
groups = json.load(groupsFile)
allWords = ''
#minLength = 10
#collocThresh = 30
minLength = random.randint(1, 12)
collocThresh = random.randint(1,100)


def postCloud():
    postText = ''
    for a in posts:
        try:
            for b in a['data']:
                postText = postText + b['post'] + ' '
        except:
            continue
        
    postText = re.sub(r'http\S+', '', postText)    
    wordcloud = WordCloud(min_word_length=minLength, collocation_threshold=collocThresh, 
                          width = 1920, height = 1080,
                          background_color ='black',
                          stopwords = stopwords,
                          min_font_size = 10).generate(postText)
            
    fig = plt.figure(figsize = (19.2, 10.8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
      
    plt.show()
    fileName = 'posts.' + str(minLength) + '.' + str(collocThresh) + '.png'
    fig.savefig(fileName)
    return(postText)

def commentCloud():
    commentText = ''
    for a in comments['comments']:
        try:
            for b in a['data']:
                commentText = commentText + b['comment']['comment'] + ' '
        except:
            continue
    commentText = re.sub(r'http\S+', '', commentText)    
    wordcloud = WordCloud(min_word_length=minLength, collocation_threshold=collocThresh, 
                          width = 1920, height = 1080,
                          background_color ='black',
                          stopwords = stopwords,
                          min_font_size = 10).generate(commentText)
            
    fig = plt.figure(figsize = (19.2, 10.8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
      
    plt.show()
    fileName = 'comments.' + str(minLength) + '.' + str(collocThresh) + '.png'
    fig.savefig(fileName)
    return(commentText)
    
def groupCloud():
    groupText = ''
    for a in groups['group_posts']['activity_log_data']:
        try:
            for b in a['data']:
                                  
                groupText = groupText + b['comment']['comment'] + ' '
                
        except:
            continue
    groupText = re.sub(r'http\S+', '', groupText)    
    wordcloud = WordCloud(min_word_length=minLength, collocation_threshold=collocThresh, 
                          width = 1920, height = 1080,
                          background_color ='black',
                          stopwords = stopwords,
                          min_font_size = 10).generate(groupText)
            
    fig = plt.figure(figsize = (19.2, 10.8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
      
    plt.show()
    fileName = 'group.' + str(minLength) + '.' + str(collocThresh) + '.png'
    fig.savefig(fileName)
    return(groupText)
    
def allWordsCloud():
    comments = commentCloud()
    posts = postCloud()
    groups = groupCloud()
    allWords = comments + posts + groups
    allWords = re.sub(r'http\S+', '', allWords)    
    wordcloud = WordCloud(min_word_length=minLength, collocation_threshold=collocThresh, 
                          width = 1920, height = 1080,
                          background_color ='black',
                          stopwords = stopwords,
                          min_font_size = 10).generate(allWords)
            
    fig = plt.figure(figsize = (19.2, 10.8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
      
    plt.show()
    fileName = 'all.' + str(minLength) + '.' + str(collocThresh) + '.png'
    fig.savefig(fileName)
    
allWordsCloud()
    