#simulation
import random as rnd
import Seattle as sea
import numpy as N
import matplotlib.pyplot as plt

deltaTime = 1
totalTime = 20
time = int(totalTime/deltaTime)

# Function returns an array of the child age distributions at each phase of the simulation
# Child age dist should be between 0.13 and 0.25
def childAgeDist(initialChildrenValue):
    randNums = N.random.uniform(-0.02, 0.02, time)
    retVal = N.zeros(time)
    retVal[0] = initialChildrenValue
    # For each year, update the child age dist
    for year in range(1, time):
        temp = retVal[year-1] + randNums[year-1]
        # Keep child age dist between 0.13 and 0.25
        temp = max(temp, .13)
        temp = min(temp, .25)
        retVal[year] = temp
    return retVal# Function returns an array of the child age distributions at each phase of the simulation


# Poverty rate should be between 0.09 and 0.23
def povertyRate(initialPovertyRate):
    randNums = N.random.uniform(-0.02, 0.02, time)
    retVal = N.zeros(time)
    retVal[0] = initialPovertyRate
    # For each year, update the poverty rate
    for year in range(1, time):
        temp = retVal[year-1] + randNums[year-1]
        # Keep poverty rate between 0.09 and 0.23
        temp = max(temp, .09)
        temp = min(temp, .23)
        retVal[year] = temp
    return retVal

# Job distribution increases at about 2% to 2.5% a year.
def job_dist(jobs):
    job_array = N.zeros(time)
    job_array[0] = jobs
    lower_bound = 0.02
    upper_bound = 0.025
    for year in range(1, time):
        #get a random value between 2% to 2.5%
        random_job_increase = N.random.uniform(lower_bound ,upper_bound)
        temp = job_array[year - 1] * random_job_increase
        job_array[year] = int(job_array[year - 1] + temp)
        lower_bound -=0.2
        upper_bound -=0.01

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

<<<<<<< HEAD
def main():
    adultDist= (1-childAgeDist(sea.children))
    adults = adultDist[0]*sea.population
    population = sea.population
    total_jobs = job_dist(sea.jobs)
    for i in range (time):
        migrants = (1-total_jobs[i]/adults)*total_jobs[i]
        population += migrants 
        adults = int(adultDist[i]*population)
        print (int(population))
=======

# Return an array of how many migrants the city gains/loses yearly
def migrants():
    numAdults = (1-childAgeDist(sea.children))*sea.population
    for i in range (int(totalTime/deltaTime)):
        numAdults [i] = int (numAdults[i])
    total_jobs = job_dist(sea.jobs)
    migrants = (1 - total_jobs/numAdults)*sea.jobs
    return migrants


# Generates a plot, showing the population, unemployment rate, and poverty rate throughout the simulation
def plot(population, unemploymentRate, povertyRate):
    x = N.linspace(2018, 2018+totalTime, totalTime/deltaTime)

    plt.subplot(3, 1, 1)
    plt.plot(x, population, 'o-')
    plt.title('US Migration Simulator Lite')
    plt.ylabel('Population')

    plt.subplot(3, 1, 2)
    plt.plot(x, unemploymentRate, 'o-')
    plt.ylabel('Unemployment Rate')

    plt.subplot(3, 1, 3)
    plt.plot(x, povertyRate, 'o-')
    plt.xLabel('Year')
    plt.ylabel('Poverty Rate')


# def simulate():



# def main():

>>>>>>> 5f3014569b1872591c87180742bc5727f6c8a658
    
#test
# print ("\nChild age distribution:\n", childAgeDist(sea.children)*100)
# print ("\nPoverty rate :\n", povertyRate(sea.povertyRate)*100)
# print ("\nJob distribution :\n", job_dist(sea.jobs))
main()
