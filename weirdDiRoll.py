# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 16:53:55 2021

@author: jared
"""

import random
import seaborn as sns
import matplotlib.pyplot as plt

def rollWeirdDi(amount):
    rolls = []
    for i in range(0,amount):
        x = random.randint(1,12)
        for u in range(0,7):
            x += random.randint(1,20)
        rolls.append(x)
        
    return rolls 

def randomizeTotals(amount):
    minRoll = 8
    maxRoll = 152
    result = []
    for i in range(0, amount):
        result.append(random.randint(minRoll, maxRoll))
    return result
        
def distPlotRolls(amount):
    fig = sns.distplot(rollWeirdDi(amount), bins=144)
    plt.title("Distribution of rolls")
    plt.xlabel("Value of roll")
    plt.ylabel("Number of times rolled")
    plt.show()
    
    return fig
    
def randomPlot(amount):
    fig = sns.distplot(randomizeTotals(amount), bins=144)
    plt.title("Distribution of random selection of values")
    plt.xlabel("Value of roll")
    plt.ylabel("Number of times rolled")
    plt.show()
    
    return fig

distPlotRolls(1000000)
randomPlot(1000000)

