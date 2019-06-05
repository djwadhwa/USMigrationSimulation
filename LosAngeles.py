import csv
import numpy as np

Name = "Los Angeles"
children = 0.213       # Portion of population which is under 18 y.o.
adults = 1- children    # Portion of population which is over 18 y.o.
povertyRate = 0.204

year_list = []
crimes_list = []
rent_list = []
taxes_list = []
pop_list = []
jobs_list = []

with open ("los_angeles_data.csv") as csv_file:
    read_csv = csv.reader (csv_file, delimiter =',')
    
    for row in read_csv:
        year_list.append(int (row [0]))
        rent_list.append(int (row [1]))
        taxes_list.append(float (row [2]))
        crimes_list.append(int (row [3]))
        pop_list.append(int (row[4]))
        jobs_list.append(int(row[5]))
        
population = pop_list[0]
print(pop_list)

jobs =  jobs_list[0]
#job_range = (.02, .025)
job_std_percentage = np.std(jobs_list[:-1])/np.mean(jobs_list)
job_range = (-job_std_percentage, job_std_percentage)

rent = rent_list[0]
rent_std_percentage = np.std(rent_list[:-1])/np.mean(rent_list)
rent_range = (-rent_std_percentage, rent_std_percentage)

crimes = crimes_list[0]
crimes_std_percentage = np.std (crimes_list[:-1])/np.mean(crimes_list)
crimes_range = (-crimes_std_percentage, crimes_std_percentage)

taxes = taxes_list[0]
taxes_std_percentage = np.std(taxes_list [:-1])/np.mean(taxes_list)
taxes_range = (0, taxes_std_percentage)
print(taxes_list)
