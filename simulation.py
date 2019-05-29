#simulation
import random as rnd
import Seattle as sea
import numpy as N

deltaTime = 1
totalTime = 20

def age_dist(population, children, adults):
    randNum = rnd.uniform(-1,1)
    print(randNum)

# Function returns an array of the child age distributions at each phase of the simulation
def childAgeDist(initialPopulation, children, adults):
    randNums = rnd.uniform(-1, 1, totalTime / deltaTime-1)
    retVal = N.zeros(totalTime / deltaTime)
    retVal[0] = initialPopulation
    for year in range(1, totalTime/deltaTime):
        retVal[year] = retVal[year-1] + randNums[year-1]
    print(retVal)
    
#test    
for i in range (10):   
    age_dist(sea.population, sea.children, sea.adults)