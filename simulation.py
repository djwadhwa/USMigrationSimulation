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
    return retVal# Function returns an array of the child age distributions at each phase of the simulation


# Poverty rate should be between 0.09 and 0.23
def povertyRate(initialPovertyRate):
    randNums = N.random.uniform(-0.02, 0.02, int(totalTime / deltaTime))
    retVal = N.zeros(int(totalTime / deltaTime))
    retVal[0] = initialPovertyRate
    # For each year, update the poverty rate
    for year in range(1, int(totalTime / deltaTime)):
        temp = retVal[year-1] + randNums[year-1]
        # Keep poverty rate between 0.09 and 0.23
        temp = max(temp, .09)
        temp = min(temp, .23)
        retVal[year] = temp
    return retVal

# Job distribution increases at about 2.5% a year.
def job_dist(jobs):
    job_array = N.zeros(int(totalTime / deltaTime))
    job_array[0] = jobs
    
    for year in range(1, int(totalTime / deltaTime)):
        temp = job_array[year - 1] * 0.025
        job_array[year] = int(job_array[year - 1] + temp)

    return job_array

def annualWater(population, childRate, adultRate):
    waterPerDayForKids = ( 7 + 10 + 14 ) / 3 * 0.236 #in litre
    waterPerDayForAdults = 3.7 #in litre
    annualWaterForKids = waterPerDayForKids * (population * childRate)
    annualWaterForAdults = waterPerDayForAdults * (population * adultRate)
    totalWater = annualWaterForAdults + annualWaterForKids
    return totalWater

#test
print ("\nChild age distribution:\n", childAgeDist(sea.children)*100)
print ("\nPoverty rate :\n", povertyRate(sea.povertyRate)*100)
print ("\nJob distribution :\n", job_dist(sea.jobs))
