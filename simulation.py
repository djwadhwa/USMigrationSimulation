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
DEFAULT_NUM_YEARS = 13


def age_dist(prev_child_percentage, lower_bound = 0.13, upper_bound = 0.25):
    """ Calculate a prediction for the age distribution of children in the
    population in the next year.

    Args:
        prev_child_percentage (int):The current child age distribution in the
                                    city
        lower_bound (float):        The lower bound for the possible age
                                    distribution of children in the population
        upper_bound (float):        The upper bound for the possible age
                                    distribution of children in the population

    Returns:
        new_child_age_dist (float): The predicted new child age distribution in
                                    the city
    """
    rand = rnd.uniform(-0.02, 0.02)

    # Keep child age dist between 0.13 and 0.25
    new_child_age_dist = prev_child_percentage + rand
    if new_child_age_dist > upper_bound:
        new_child_age_dist = min(new_child_age_dist, upper_bound)
    elif new_child_age_dist < lower_bound:
        new_child_age_dist = max(new_child_age_dist, lower_bound)

    # Function returns an array of the child age distributions at each phase of the simulation
    return new_child_age_dist


def natural_pop_growth (population):
    """ Calculate a prediction for how much the population naturally grows
    within a year.

    Prediction based on official rates of US national population growth

    Args:
        population (int):           The current population of the city

    Returns:
        total_natural_pop (int):    The predicted new population after
                                    natural growth
    """
    delta_natural_pop = population * rnd.uniform \
    (us.natural_population_growth[0], us.natural_population_growth[1])

    total_natural_pop = population + delta_natural_pop

    return total_natural_pop


def update_jobs(jobs, job_range):
    """ Calculate a prediction for the next year's number of jobs based on the
    current number of jobs, and the city's job range.

    Prediction made using monte carlo method.

    Args:
        jobs (float):           The current number of jobs in the city
        job_range (List):       A List of 2 values representing the upper and
                                lower bounds of the percentage by which jobs
                                increase yearly

    Returns:
        total_jobs (float):     The predicted new number of jobs in the city
    """
    lower_bound = job_range[0];
    upper_bound = job_range[1];

    random_jobs = N.random.normal(lower_bound ,upper_bound)
    rand_delta = jobs * random_jobs
    total_jobs = int(jobs + rand_delta)

    return total_jobs


def update_crimes(crimes, crime_range):
    """ Calculate a prediction for the next year's crime rate based on the
    current crime rate, and the city's crime range.

    Prediction made using monte carlo method.

    Args:
        crimes (float):         The current tax rate of the city
        crime_range (List):     A List of 2 values representing the upper and
                                lower bounds of that city's crime range.

    Returns:
        total_crimes (float):   The predicted new crime rate for the city
    """
    lower_bound = crime_range[0];
    upper_bound = crime_range[1];

    random_crimes = N.random.uniform(lower_bound ,upper_bound)
    rand_delta = crimes * random_crimes
    total_crimes = int(crimes + rand_delta)

    return total_crimes


def update_rent(rent, rent_range):
    """ Calculate a prediction for the next year's average rent based on the
    current rent, and the city's rent range.

    Prediction made using monte carlo method.

    Args:
        rent (float):          The current tax rate of the city
        rent_range (List):       A List of 2 values representing the upper and
                                lower bounds of that city's rent.

    Returns:
        total_rent (float):    The predicted new average rent for the city
    """
    lower_bound = rent_range[0];
    upper_bound = rent_range[1];

    random_rent = N.random.normal(lower_bound ,upper_bound)
    rand_delta = rent * random_rent
    total_rent = int(rent + rand_delta)

    return total_rent


def update_taxes(taxes, tax_range):
    """ Calculate a prediction for the next year's tax rate based on the
    current tax rate, and the city's tax range.

    Prediction made using monte carlo method.

    Args:
        taxes (float):          The current tax rate of the city
        tax_range (List):       A List of 2 values representing the upper and
                                lower bounds of that city's taxes.

    Returns:
        total_taxes (float):    The predicted new tax rate for the city
    """
    lower_bound = tax_range[0];
    upper_bound = tax_range[1];

    random_taxes = N.random.uniform(lower_bound ,upper_bound)
    rand_delta = taxes * random_taxes
    total_taxes = taxes + rand_delta

    return total_taxes


def water_consumption(population, adult_dist):
    """ Based on the given factors, calculate a prediction for the yearly
    water intake in the city.

    Yearly water intake is indicated by the city's age distribution of
    children and adults.

    Args:
        population (int):               The population size of the city
        adults_dist (float):            Fraction of the city's population which
                                        is 18+ years of age

    Returns:
        total_annual_water (int):       The predicted number of litres of water
                                        consumed yearly in the city
    """

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
    """ Based on the given factors, calculate a prediction for the yearly
    caloric intake in the city.

    Yearly caloric intake is indicated by the city's age distribution of
    children and adults.

    Args:
        population (int):               The population size of the city
        adults_rate (float):            Fraction of the city's population which
                                        is 18+ years of age

    Returns:
        total_annual_calories (int):    The predicted number of calories
                                        consumed yearly in the city
    """

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


def plotter (city, pop_array, water_array, food_array, time_array):
    """ Plot the population across years as predicted by the model, alongside
    the actual population values from the data.

    Args:
        city:                   The class representing the city being modeled
        pop_array (List):       Population values as predicted by the model
        water_array (List):     Water values as predicted by the model
        food_array (List):      Food values as predicted by the model
        time_array (List):      Year values for the model
    """
    fig1, ax1 = plt.subplots()
    ax1.plot(time_array, pop_array)

    # Make copy of city.pop_list, but of the desired size
    city_pop_list = N.zeros(len(time_array))
    for i in range(0, len(city_pop_list)):
        city_pop_list[i] = city.pop_list[i]

    ax1.plot (time_array, city_pop_list)
    ax1.set_title(city.Name + "'s population growth due to migration over "+
    str(len(time_array))+" years")
    ax1.set_xlabel("Time (years)")
    ax1.set_ylabel("Population")

    fig2, ax1 = plt.subplots()
    ax1.plot(time_array[1:], water_array[1:])
    ax1.set_title(city.Name + "'s water consumption over "+
    str(len(time_array))+" years")
    ax1.set_xlabel("Time (years)")
    ax1.set_ylabel("Water consumed (100 million gallons)")

    fig3, ax1 = plt.subplots()
    ax1.plot(time_array[1:], food_array[1:])
    ax1.set_title(city.Name + "'s food consumption over "+
    str(len(time_array))+" years")
    ax1.set_xlabel("Time (years)")
    ax1.set_ylabel("Food consumed (100 billion consumed)")
    plt.show()


def printer(city, population_array, time_array, output_file_name = None):
    """ Print the population across years as predicted by the model.

    Args:
        city:                   The class representing the city being modeled
        population_array (List):Population values as predicted by the model
        time_array (List):      Year values for the model
        output_file_name (str): The file to which output should be written
    """
    # If outputting to stdout
    if(output_file_name == None):
        print (city.Name+"'s population over " + str(len(time_array)) + " years")
        for i in range(0, len(time_array)-1):
            print (time_array[i], "\t", population_array[i] )
    # If writing to a file
    else:
        file = open(output_file_name, "w")
        file.write(city.Name+"'s population over " + str(len(time_array)) + " years")
        for year in time_array:
            line = str(year, "\t", str(population_array[year]) )
            file.write(line)
        file.close()


def calculate_migrants(city, free_jobs, crimes, rent, taxes):
    """ Based on the given factors, calculate a prediction for the number of
    incoming migrants to the city.

    Args:
        city:               The class representing the city being modeled
        free_jobs (float):  Number of available jobs this year in the city
        crimes (float):     Number of crimes committed this year in the city
        rent (float):       Average rent cost this year in the city
        taxes (float):      Average tax this year in the city

    Returns:
        A float
    """
    if (city == sea):
        return 0.4*free_jobs - (10/taxes)- 0.25*crimes - 0.8*rent
    elif(city == chi):
        return 0.2*free_jobs - (100/taxes) - 0.45*crimes - 0.8*rent
    else:
        return 0.35*free_jobs - (100/taxes) - .45*crimes - 40*rent


def model(city, num_years = DEFAULT_NUM_YEARS, trials = 100):
    """ Run the model on a city, predict yearly population and water.

    Args:
        city:               The class representing the city being modeled
        num_years (int):         Number of years over which to run the model
        trials (int):       Number of trials for which to run the model

    Returns:
        city:               an int representing the absolute error of the model
        pop (List)          A list of ints representing population size across years
        wat (List)          A list of ints representing water amount across years
        time_array (List)   A list of ints representing years which are modeled
    """
    population_average = []
    pop = N.zeros(num_years)
    wat = N.zeros(num_years)
    food = N.zeros(num_years)
    water_average = []
    food_average = []

    # Make copy of city.year_list, but of the desired size
    year_list = N.zeros(num_years)
    for i in range(num_years):
        year_list[i] = city.year_list[i]

    for trial in range(trials):
        adult_dist = city.adults
        total_jobs = city.jobs
        crimes = city.crimes
        rent = city.rent
        taxes = city.taxes

        population_array = N.zeros(num_years)
        water_array = N.zeros(num_years)
        food_array = N.zeros(num_years)
        population_array[0] = city.population

        #0.174 is the amount of jobs that are worked by migrants
        for i in range (1, num_years):
            free_jobs = total_jobs*us.migrant_jobs
            migrants = calculate_migrants(city, free_jobs, crimes, rent, taxes)
            # Account for natural growth
            population_array[i] = natural_pop_growth(population_array[i-1])
            population_array[i] += migrants

            # Update factors every year
            adult_dist = 1 - age_dist(1-adult_dist)
            total_jobs = update_jobs(total_jobs, city.job_range)
            crimes = update_crimes(crimes, city.crimes_range )
            rent = update_rent(rent, city.rent_range)
            taxes = update_taxes (taxes, city.taxes_range)

            #output
            water_array[i] = water_consumption (population_array[i-1], adult_dist)
            food_array[i] = food_consumption (population_array[i-1], adult_dist)

        population_average.append(population_array)
        water_average.append(water_array)
        food_average.append(food_array)

    for i in range(trials):
        for j in range(num_years):
            pop[j]+= population_average[i][j]
            wat[j]+=water_average[i][j]
            food[j]+=food_average[i][j]
    pop /= trials
    wat /= trials
    food /= trials
    return (city, pop, wat, food, year_list)


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
    for i in range(len(time_array)-1):
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
    for i in range(len(time_array)-1):
        population_error = population_error + abs(city.pop_list[i] - population_array[i]) /abs (population_array[i])

    population_error /= len (population_array)
    return population_error


def runModelTest(city, output_file_name = None, num_years = DEFAULT_NUM_YEARS, trials = 100):
    """ Function to run the model, calculate absolute & relative errors, and output the results
    in both text and a graph.

    Args:
        city:                   The class representing the city being modeled
        output_file_name (str): The file to which output should be written
        num_years (int):        Number of years over which the model should run
        trials (int):           Number of trials for which the model should run
    """
    (city, pop, wat, food, time_array) = model(city, num_years, trials)
    # Calculate error
    absolute_error = absoluteError(city, pop, time_array)
    relative_error = relativeError(city, pop, time_array)
    # Print output
    printer (city, pop, time_array, output_file_name)
    # Plot graph
    plotter (city, pop, wat, food, time_array)
    # If outputting to stdout
    if(output_file_name == None):
        print("Absolute Error: ", absolute_error)
        print("Relative Error: ", relative_error*100, "%")
    # If writing to a file
    else:
        file = open(output_file_name, "a")
        file.write("Absolute Error: ", absolute_error)
        file.write("Relative Error: ", relative_error)
        file.close()


#tester
runModelTest(sea)
runModelTest(chi)