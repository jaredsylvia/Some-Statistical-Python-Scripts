# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 16:53:55 2021

@author: jared
"""

import random
import seaborn as sns
import matplotlib.pyplot as plt
import numpy

def rollWeirdDi(dice, amount, modifier):    # A function that rolls dice in list identified as dice a number of times identified as amount plus modifier for roll
                           
    rolls = []
    
    for i in range(0,amount):
        currentRoll = 0
        for roll in dice: # For each set of die listed do the following
            
            rollList = roll.split('d') #Split number of and side of die
            
            for di in range(0, int(rollList[0])): #for every di in roll do the following
                currentRoll += (random.randint(1,int(rollList[1]))) #add a number between 1 and the highest side of di to currentRoll plus modifier
                
        rolls.append(currentRoll + modifier) #Append total to rolls[]
    
    return rolls 

def randomizeTotals(amount, minRoll, maxRoll): # A function that randomly generates a number between two other numbers x amount of times
    result = []
    for i in range(0, amount):
        result.append(random.randint(minRoll, maxRoll))
    return result
        
def disPlotRolls(rolls):
    rolls.sort()
    fig = sns.displot(rolls, bins=(int(rolls[-1]) - int(rolls[0])))
    plt.title("Distribution of rolls")
    plt.xlabel("Value of roll")
    plt.ylabel("Number of times rolled")
    plt.show()
    
    return fig
    
def randomPlot(amount, minRoll, maxRoll):
    fig = sns.displot(randomizeTotals(amount, minRoll, maxRoll), bins=(maxRoll - minRoll))
    plt.title("Distribution of random selection of values")
    plt.xlabel("Value of roll")
    plt.ylabel("Number of times rolled")
    plt.show()
    
    return fig

def printPerRollStats(rolls): 
    print('Roll/Freq')
    fdist=dict(zip(*numpy.unique(rolls, return_counts=True)))
    highestFreq = [0,0]
    
    for key in fdist:
        print(str(key) + '/' + str(fdist[key]))
        if(fdist[key] > highestFreq[1]):
            highestFreq = [key, fdist[key]]
    #print(highestFreq)
    print('The most frequently occuring number was ' + str(highestFreq[0]) + \
          ' being rolled ' + str(highestFreq[1]) + ' times.')


dice = ['3d6', '2d20', '3d100'] # Conventional tabletop format (3d6 = 3 six sided, 2d10 = 2 ten sided, 1d20 = 1 twenty sided, etc.,) in a list
modifier = 0 #Positive or negative integer 0 if none
numOfRolls = 100000 # The higher the more accurate, should be higher than variation of dice - could slow down computer with large numbers


rolls = rollWeirdDi(dice, numOfRolls, modifier) # list of rolls matching parameters

disPlotRolls(rolls) # Generage a graph of results

printPerRollStats(rolls)# Per roll stats



