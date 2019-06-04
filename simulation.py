#simulation
import numpy.random as rnd
import Seattle as sea
import Chicago as chi
import LosAngeles as la
import NewYork as ny
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
    if temp > upper_bound:
        temp = min(temp, upper_bound)
    elif temp < lower_bound:
        temp = max(temp, lower_bound)
    
    # Function returns an array of the child age distributions at each phase of the simulation  
    return temp

def natural_pop_growth (population):
    delta_natural_pop = population * rnd.uniform \
    (us.natural_population_growth[0], us.natural_population_growth[1])
    
    total_natural_pop = population + delta_natural_pop
    
    return total_natural_pop
    
# Job distribution increases at about 2% to 2.5% a year.
def update_jobs(jobs, job_rate):
    lower_bound = job_rate[0];
    upper_bound = job_rate[1];
    
    random_jobs = N.random.uniform(lower_bound ,upper_bound)
    rand_delta = jobs * random_jobs
    total_jobs = int(jobs + rand_delta)
    
    return total_jobs

def update_crimes(crimes, crime_rate):
    lower_bound = crime_rate[0];
    upper_bound = crime_rate[1];
    
    random_crimes = N.random.uniform(lower_bound ,upper_bound)
    rand_delta = crimes * random_crimes
    total_crimes = int(crimes + rand_delta)
    
    return total_crimes

def update_rent(rent, rent_rate):
    lower_bound = rent_rate[0];
    upper_bound = rent_rate[1];
    
    random_rent = N.random.uniform(lower_bound ,upper_bound)
    rand_delta = rent * random_rent
    total_rent = int(rent + rand_delta)
    
    return total_rent
    
def update_taxes(taxes, tax_rate):
    lower_bound = tax_rate[0];
    upper_bound = tax_rate[1];
    
    random_taxes = N.random.uniform(lower_bound ,upper_bound)
    rand_delta = taxes * random_taxes
    total_taxes = taxes + rand_delta
    
    return total_taxes

# Return number of litres of water that would be drunk annually by a population
# of theindicated size, with the indicated distribution of children and adults
def water_consumption(population, adult_dist):
    daily_water_children= ( 7 + 10 + 14 ) / 3 * 0.236 * 0.264172     #in gallons
    daily_water_adults= 3.7 * 0.264172                           #in gallons
    
    annual_water_adults = daily_water_adults * (population * adult_dist) * 365
    annual_water_children = daily_water_children * \
    (population * 1 - adult_dist) * 365
    total_annual_water = annual_water_adults + annual_water_children
    
    # return (annual_water_children, annual_water_adults, total_annual_water)
    return total_annual_water

def food(population, child_rate):
    return 0
    
    
def plotter (city, popualtion_array, water_array, time_array):
    fig1, ax1 = plt.subplots()
    ax1.plot(time_array, popualtion_array)
    ax1.plot (N.arange(14), city.pop_list)
    ax1.set_title(city.Name + "'s population growth due to migration over "+  
    str(len(time_array))+" years")
    ax1.set_xlabel("Time (years)")
    ax1.set_ylabel("Population")
    # fig2, ax1 = plt.subplots()
    # ax1.plot(time_array, water_array)
    # ax1.set_title(city.Name + "'s water consumption over "+  
    # str(len(time_array))+" years")
    # ax1.set_xlabel("Time (years)")
    # ax1.set_ylabel("Water consumed (100 million gallons)")
    plt.show()
    
def printer(city, population_array, time_array):
    print (city.Name+"s poulation over " + str(len(time_array)) + "years")
    for year in time_array:
        print (2006+year, "\t", population_array[year] )

def calculate_migrants(free_jobs, crimes, rent, taxes):
    # return free_jobs * 1/crimes * rent *taxes
    # return (0.7*free_jobs - 0.6*crimes - 7*rent - 30000*taxes)
    return 2*free_jobs


def main(city, time = 20, trials = 100):
    """ Run the model on a city, predict yearly population and water.

    Args:
        city:               The class representing the city being modeled
        time (int):         Number of years over which to run the model
        trials (int):       Number of trials for which to run the model

    Returns:
        city:               an int representing the absolute error of the model
        pop (List)          A list of ints representing population size across years
        wat (List)          A list of ints representing water amount across years
        time_array (List)   A list of ints representing years which are modeled
    """
    population_average = []
    pop = []
    wat =[]
    water_average = []
    for trial in range(trials):
        adult_dist = city.adults
        adults = city.adults*city.population
        
        total_jobs = city.jobs
        crimes = city.crimes
        rent = city.rent
        taxes = city.taxes
        
        
        time_array = N.arange(time)
        population_array = N.zeros(time)
        water_array = N.zeros(time)
        population_array[0] = city.population
        
        for year in range (1, time):
            #0.174 
            free_jobs = total_jobs*.174 + (total_jobs-adults)
            migrants = calculate_migrants(free_jobs, crimes, rent, taxes)
            # print (migrants/population_array[year-1])
            # ratio = 1 - (migrants/population_array[year-1])
            # migrants *= ratio
            population_array[year] = natural_pop_growth(population_array[year-1]) 
            population_array[year] += migrants
            # print (migrants / population)
            #output
            water_array[year] = int (water_consumption (population_array[year], adult_dist))
            
            #update every year
            adult_dist = 1 - age_dist(1-adult_dist)
            adults = adult_dist * population_array[year]
            total_jobs = update_jobs(total_jobs, city.job_range)
            crimes = update_crimes(crimes,city.crimes_range )
            rent = update_rent(rent, city.rent_range)
            taxes = update_taxes (taxes, city.taxes_range)
            
        population_average.append(population_array)
        water_average.append(water_array)
        
    for i in range(time):
        pop.append(N.average(population_average[:][i]))
        wat.append(N.average(water_average[:][i]))
        
    return (city, pop, wat, time_array)


def absoluteError(city, population_array, time_array):
    """ Function to return the absolute error of a city's population model.

    Absolute error = |correct - result|

    Args:
        city:                       The class representing the city being modeled
        population_array (list):    A list of ints representing population size across years
        time_array (list):          List of ints representing years which are modeled

    Returns:
        population_error (int):     an int representing the absolute error of the model
    """
    population_error = 0
    for i in time_array:
        population_error = population_error + abs(city.pop_list[i] - population_array[i])
    return population_error


def relativeError(city, population_array, time_array):
    """ Function to return the relative error of a city's population model.

    Relative error = |correct - result| / |correct|

    Args:
        city:                       The class representing the city being modeled
        population_array (list):    A list of ints representing population size across years
        time_array (list):          List of ints representing years which are modeled

    Returns:
        population_error (int):     an int representing the relative error of the model
    """
    population_error = 0
    for i in time_array:
        population_error = population_error + (abs(city.pop_list[i] - population_array[i])
                                               / abs(city.pop_list[i]))
    return population_error
    
#test
# print ("\nChild age distribution:\n", childAgeDist(sea.children)*100)
# print ("\nPoverty rate :\n", povertyRate(sea.povertyRate)*100)
# print ("\nJob distribution :\n", job_dist(sea.jobs))

main(sea, 13)
(city, pop, wat, time_array) = main(sea, 13)
# printer (city, pop, time_array)
plotter (city, pop, wat, time_array)


# main(chi, 13)
# main(la, 13)
# main(ny, 13)

