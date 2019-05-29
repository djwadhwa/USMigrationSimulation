#simulation
import random as rnd
import Seattle as sea
import numpy as N

deltaTime = 1
totalTime = 20

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

# Job distribution increases at about 2% to 2.5% a year.
def job_dist(jobs):
    job_array = N.zeros(int(totalTime / deltaTime))
    job_array[0] = jobs
    
    for year in range(1, int(totalTime / deltaTime)):
        #get a random value between 2% to 2.5%
        random_job_increase = N.random.uniform(0.020 ,0.025)
        temp = job_array[year - 1] * random_job_increase
        job_array[year] = int(job_array[year - 1] + temp)

    return job_array

# Return number of litres of water that would be drunk annually by a population of the
# indicated size, with the indicated distribution of children and adults
def annualWater(population, childRate, adultRate):
    waterPerDayForKids = ( 7 + 10 + 14 ) / 3 * 0.236 * 0.264172     #in gallons
    waterPerDayForAdults = 3.7 * 0.264172                           #in gallons
    annualWaterForKids = waterPerDayForKids * (population * childRate) * 365
    annualWaterForAdults = waterPerDayForAdults * (population * adultRate) * 365
    totalWater = annualWaterForAdults + annualWaterForKids
    return totalWater

def main():
    adults = (1-childAgeDist(sea.children))*sea.population
    for i in range (int(totalTime/deltaTime)):
        adults [i] = int (adults[i])
    total_jobs = job_dist(sea.jobs)
    migrants = (1 - total_jobs/adults)*sea.jobs
    return migrants
    
#test
# print ("\nChild age distribution:\n", childAgeDist(sea.children)*100)
# print ("\nPoverty rate :\n", povertyRate(sea.povertyRate)*100)
# print ("\nJob distribution :\n", job_dist(sea.jobs))
print(main())
