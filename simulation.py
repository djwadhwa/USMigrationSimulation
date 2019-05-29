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
# Child age dist should be between 0.13 and 0.25
def childAgeDist(initialChildrenValue):
    randNums = rnd.uniform(-0.1, 0.1, totalTime / deltaTime-1)
    retVal = N.zeros(totalTime / deltaTime)
    retVal[0] = initialChildrenValue
    # For each year, update the child age dist
    for year in range(1, totalTime/deltaTime):
        temp = retVal[year-1] + randNums[year-1]
        # Keep child age dist between 0.13 and 0.25
        temp = max(temp, 13)
        temp = min(temp, 25)
        retVal[year] = temp
    print(retVal)
    return retVal
    
#test    
for i in range (10):   
    age_dist(sea.population, sea.children, sea.adults)