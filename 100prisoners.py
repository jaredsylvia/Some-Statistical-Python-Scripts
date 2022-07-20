# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 19:13:21 2022

@author: jared
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class Prison:
    def __init__(self, numOfPrisoners):
        self.numOfPrisoners = numOfPrisoners

        self.prisonerList = np.random.permutation(numOfPrisoners)[:numOfPrisoners].tolist()
        self.prisonerDict = {}
        for i in range(0,numOfPrisoners):
            self.prisonerDict[i] = self.prisonerList[i]
            
    def halfNhalf(self):       #Returns how many prisoners succeeded
        
        success = 0
        failure = 0
        
        for i in range(0,round(self.numOfPrisoners/2)):
            guessPrisoners = np.random.permutation(
                self.numOfPrisoners)[:round(self.numOfPrisoners/2)].tolist()
            if i in guessPrisoners:
                success += 1
            else:
                failure += 1
                
        
        return success
        
    def startWithSelf(self): # Simulates selecting boxes in order
        guesses = {}
        totalCorrect = 0
        for i in range(0,self.numOfPrisoners):
            guesses["Prisoner {}".format(i)] = []
        
            
            currentGuess = self.prisonerList[i]
            totalGuesses = 1
            while currentGuess != i and totalGuesses <= 50:
        
                
                guesses["Prisoner {}".format(i)].append(self.prisonerList[currentGuess])
        
                if self.prisonerList[currentGuess] == i:
                   totalCorrect += 1
                  
                currentGuess = self.prisonerList[currentGuess]
                
                totalGuesses += 1
        
        return totalCorrect

def disPlot(attempts, title):
    attempts.sort()
    fig = sns.displot(attempts, bins=(int(attempts[-1]) - int(attempts[0])))
    plt.title(title)
    plt.xlabel("Number of successful individuals")
    
    plt.show()
    return fig

if __name__ == '__main__':
    
    halfAtRandomResults = []
    startWithSelfResults = []
    for i in range(0,1000):
        Prison100 = Prison(100)
        halfResults = Prison100.halfNhalf()
        startWSelfResults = Prison100.startWithSelf()
        halfAtRandomResults.append(halfResults)
        startWithSelfResults.append(startWSelfResults)

    disPlot(halfAtRandomResults, "Selecting half at random.")
    disPlot(startWithSelfResults, "Starting with own number.")


