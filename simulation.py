#simulation
import numpy.random as rnd
import Seattle as sea
import us 
import numpy as N
import matplotlib.pyplot as plt

deltaTime = .5
totalTime = 20

# Function returns an array of the child age distributions at each phase of the simulation
# Child age dist should be between 0.13 and 0.25
def age_dist(prev_child_percentage, lower_bound = 0.13, upper_bound = 0.25):
    rand = rnd.uniform(-0.02, 0.02)
    
    # Keep child age dist between 0.13 and 0.25
    temp = prev_child_percentage + rand
    temp = max(temp, lower_bound)
    temp = min(temp, upper_bound)
    
    # Function returns an array of the child age distributions at each phase of the simulation  
    return temp

# # Poverty rate should be between 0.09 and 0.23
# def povertyRate(initialPovertyRate):
#     randNums = rnd.uniform(-0.02, 0.02, time)
#     retVal = N.zeros(time)
#     retVal[0] = initialPovertyRate
#     # For each year, update the poverty rate
#     for year in range(1, time):
#         temp = retVal[year-1] + randNums[year-1]
#         # Keep poverty rate between 0.09 and 0.23
#         temp = max(temp, .09)
#         temp = min(temp, .23)
#         retVal[year] = temp
#     return retVal

def natural_pop_growth (population):
    delta_natural_pop = population * rnd.uniform \
    (us.natural_population_growth[0], us.natural_population_growth[1])
    
    total_natural_pop = population + delta_natural_pop
    
    return total_natural_pop
    
# Job distribution increases at about 2% to 2.5% a year.
def job(jobs, job_rate):
    lower_bound = job_rate[0];
    upper_bound = job_rate[1];
    
    random_jobs = N.random.uniform(lower_bound ,upper_bound)
    rand_delta = jobs * random_jobs
    total_jobs = int(jobs + rand_delta)
    
    return total_jobs

def crime(crimes, crime_rate):
    lower_bound = crime_rate[0];
    upper_bound = crime_rate[1];
    
    random_crimes = N.random.uniform(lower_bound ,upper_bound)
    rand_delta = crimes * random_crimes
    total_crimes = int(crimes + rand_delta)
    
    return total_crimes

def rent(rent, rent_rate):
    lower_bound = rent_rate[0];
    upper_bound = rent_rate[1];
    
    random_rent = N.random.uniform(lower_bound ,upper_bound)
    rand_delta = rent * random_rent
    total_rent = int(rent + rand_delta)
    
    return total_rent
    
def taxes(taxes, tax_rate):
    lower_bound = tax_rate[0];
    upper_bound = tax_rate[1];
    
    random_taxes = N.random.uniform(lower_bound ,upper_bound)
    rand_delta = taxes * random_taxes
    total_taxes = int(taxes + rand_delta)
    
    return total_taxes

# Return number of litres of water that would be drunk annually by a population of the
# indicated size, with the indicated distribution of children and adults
def water_consumption(population, adult_dist):
    daily_water_children= ( 7 + 10 + 14 ) / 3 * 0.236 * 0.264172     #in gallons
    daily_water_adults= 3.7 * 0.264172                           #in gallons
    
    annual_water_adults = daily_water_adults * (population * adult_dist) * 365
    annual_water_children = daily_water_children * (population * 1 - adult_dist) * 365
    total_annual_water = annual_water_adults + annual_water_children
    
    return (annual_water_children, annual_water_adults, total_annual_water)

def food(population, child_rate):
    return 0
    
def calculate_migrants(jobs, crime, rent, taxes):
    return 0
    
def main(city, time):
    
    adult_dist = city.adults
    adults = city.adults*city.population
    population = city.population
    
    jobs = city.jobs
    crimes = city.crimes
    rent = city.rent
    taxes = city.taxes
    
    population_array = N.zeros(time);
    
    for i in range (time):
        migrants = calculate_migrants(jobs, crime, rent, taxes)
        population = natural_pop_growth(population) 
        population += migrants
        
        adult_dist = 1 - age_dist(1-adult_dist)
        adults = adult_dist * population
        population_array[i] = int(population)
        
    plt.plot(N.arange(time), population_array)
    print (population_array)
    plt.plot(N.arange(time), population_array)
    plt.show()


# # Generates a plot, showing the population, unemployment rate, and poverty rate throughout the simulation
# def plot(population, unemploymentRate, povertyRate):
#     x = N.linspace(2018, 2018+totalTime, totalTime/deltaTime)
# 
#     plt.subplot(3, 1, 1)
#     plt.plot(x, population, 'o-')
#     plt.title('US Migration Simulator Lite')
#     plt.ylabel('Population')
# 
#     plt.subplot(3, 1, 2)
#     plt.plot(x, unemploymentRate, 'o-')
#     plt.ylabel('Unemployment Rate')
# 
#     plt.subplot(3, 1, 3)
#     plt.plot(x, povertyRate, 'o-')
#     plt.xLabel('Year')
#     plt.ylabel('Poverty Rate')

#test
# print ("\nChild age distribution:\n", childAgeDist(sea.children)*100)
# print ("\nPoverty rate :\n", povertyRate(sea.povertyRate)*100)
# print ("\nJob distribution :\n", job_dist(sea.jobs))
main(sea, 20)
