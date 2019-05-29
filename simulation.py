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
    randNums = N.random.uniform(-0.02, 0.02, int(totalTime / deltaTime))
    retVal = N.zeros(int(totalTime / deltaTime))
    retVal[0] = initialChildrenValue
    # For each year, update the child age dist
    for year in range(1, int(totalTime / deltaTime)):
        temp = retVal[year-1] + randNums[year-1]
        # Keep child age dist between 0.13 and 0.25
        temp = max(temp, .13)
        temp = min(temp, .25)
        retVal[year] = temp
    print(retVal)
    return retVal
    
#test    
print (childAgeDist(sea.children))