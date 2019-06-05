#simulation
import numpy.random as rnd
import numpy as N
import matplotlib.pyplot as plt

import Seattle as sea
import Chicago as chi
import LosAngeles as la
import NewYork as ny
import us 

#store the number of years to simulate for
time = 13

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

    random_jobs = N.random.binomial(lower_bound ,upper_bound)
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
    
    adult_dist = 1 - age_dist(1-adult_dist)
    daily_water_children= ( 7 + 10 + 14 ) / 3 * 0.236 * 0.264172     #in gallons
    daily_water_adults= 3.7 * 0.264172                           #in gallons
    
    annual_water_adults = daily_water_adults * (population * adult_dist) * 365
    annual_water_children = daily_water_children * \
    (population * (1 - adult_dist)) * 365
    total_annual_water = annual_water_adults + annual_water_children
    
    # return (annual_water_children, annual_water_adults, total_annual_water)
    return total_annual_water

# Return number of calories intake per year total
# Indicated by age distribution of children and adults 
def food_consumption(population, adults_rate):
    
    adults_rate = 1 - age_dist(1-adults_rate)
    #counting calories suggested for children below 18-years-old
    calories_per_day_children = (1400 + 2000 + 2600 + 3200) / 4
    #counting calories suggested for adults older than 18
    calories_per_day_adults = (3000 + 3000 + 2800) / 3

    annual_calories_children = calories_per_day_children * \
        (population * (1 - adults_rate)) * 365
    annual_calories_adults = calories_per_day_adults * \
        (population * adults_rate) * 365
    total_annual_calories = annual_calories_children + annual_calories_adults
    return total_annual_calories
   
       
def plotter (city, popualtion_array, water_array, food_array, time_array):
    fig1, ax1 = plt.subplots()
    ax1.plot(time_array, popualtion_array)
    ax1.plot (N.arange(14), city.pop_list)
    ax1.set_title(city.Name + "'s population growth due to migration over "+  
    str(len(time_array))+" years")
    ax1.set_xlabel("Time (years)")
    ax1.set_ylabel("Population")
    fig2, ax1 = plt.subplots()
    ax1.plot(time_array, water_array)
    ax1.set_title(city.Name + "'s water consumption over "+  
    str(len(time_array))+" years")
    ax1.set_xlabel("Time (years)")
    ax1.set_ylabel("Water consumed (100 million gallons)")
    fig2, ax1 = plt.subplots()
    ax1.plot(time_array, food_array)
    ax1.set_title(city.Name + "'s food consumption over "+  
    str(len(time_array))+" years")
    ax1.set_xlabel("Time (years)")
    ax1.set_ylabel("Food consumed (100 billion consumed)")
    plt.show()


def printer(city, population_array, time_array, file_name = None):
    # If outputting to stdout
    if(file_name == None):
        print (city.Name+"s poulation over " + str(len(time_array)) + "years")
        for year in time_array:
            print (2006+year, "\t", population_array[year] )
    # If writing to a file
    else:
        file = open(file_name, "w")
        file.write(city.Name+"s poulation over " + str(len(time_array)) + "years")
        for year in time_array:
            line = str(2006+year, "\t", str(population_array[year]) )
            file.write(line)
        file.close()


def calculate_migrants(city, free_jobs, crimes, rent, taxes):
    if (city == sea):
        return 0.5*free_jobs - (10/taxes) - 0.25*crimes - 0.8*rent
    elif(city == chi):
        return 0.2*free_jobs - (100/taxes) - 0.45*crimes - 0.8*rent
    else:
        return free_jobs - (1000/taxes) - 2*crimes - 40*rent


def model(city, time = 20, trials = 100):
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
    pop.append(city.population)
    wat =[]
    wat.append(water_consumption(city.population, city.adults))
    food = []
    food.append(food_consumption(city.population, city.adults))
    water_average = []
    food_average = []
    for trial in range(trials):
        adult_dist = city.adults
        
        total_jobs = city.jobs
        crimes = city.crimes
        rent = city.rent
        taxes = city.taxes

        time_array = N.arange(time)
        population_array = N.zeros(time)
        water_array = N.zeros(time)
        food_array = N.zeros(time)
        population_array[0] = city.population
        #0.174 is the amount of jobs that are worked by migrants
        free_jobs = total_jobs*us.migrant_jobs
        for year in range (1, time):     
            
            migrants = calculate_migrants(city, free_jobs, crimes, rent, taxes)
            population_array[year] = natural_pop_growth(population_array[year-1]) 
            population_array[year] += migrants
              
            #update every year
            adult_dist = 1 - age_dist(1-adult_dist)
            total_jobs = update_jobs(total_jobs, city.job_range)
            crimes = update_crimes(crimes,city.crimes_range )
            rent = update_rent(rent, city.rent_range)
            taxes = update_taxes (taxes, city.taxes_range)
            free_jobs = total_jobs*us.migrant_jobs
            
            #output
            second_dist = 1 - age_dist(adult_dist)
            water_array[year] = water_consumption (population_array[year], second_dist)
            food_array[year] = food_consumption (population_array[year], second_dist)
            
        population_average.append(population_array)
        water_average.append(water_array)
        food_average.append(food_array)
        
    for i in range(0, time-1):
        pop.append(N.average(population_average[:][i]))
        wat.append(N.average(water_average[:][i]))
        food.append(N.average(food_average[:][i]))
        
    return (city, pop, wat, food, time_array)
    

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
    population_error /= len (population_array)
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
        population_error = population_error + abs(city.pop_list[i] - population_array[i]) /abs (population_array[i])
    
    population_error /= len (population_array)
    return population_error


def runModelTest(city, file_name = None):
    (city, pop, wat, food, time_array) = model(city, time)
    # Calculate error
    absolute_error = absoluteError(city, pop, time_array)
    relative_error = relativeError(city, pop, time_array)
    # Print output
    printer (city, pop, time_array, file_name)
    # Plot graph
    plotter (city, pop, wat, food, time_array)
    # If outputting to stdout
    if(file_name == None):
        print("Absolute Error: ", absolute_error)
        print("Relative Error: ", relative_error*100, "%")
    # If writing to a file
    else:
        file = open(file_name, "a")
        file.write("Absolute Error: ", absolute_error)
        file.write("Relative Error: ", relative_error)
        file.close()

#tester
runModelTest(sea)