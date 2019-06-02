import csv
import numpy as np

population = 2716000
children = 0.215        # Portion of population which is under 18 y.o.
adults = 1- children    # Portion of population which is over 18 y.o.
povertyRate = 0.206

jobs =  1200000
job_range = (.02, .025)

crimes_list = []
rent_list = []
taxes_list = []

with open ("chicago_data.csv") as csv_file:
    read_csv = csv.reader (csv_file, delimiter =',')
    
    for row in read_csv:
        rent_list.append(int (row [1]))
        taxes_list.append(float (row [2]))
        crimes_list.append(int (row [3]))
        
rent = rent_list[-1]
rent_std_percentage = np.std(rent_list[:-1])/np.mean(rent_list)
rent_range = (-rent_std_percentage, rent_std_percentage)

crimes = crimes_list[-1]
crimes_std_percentage = np.std (crimes_list[:-1])/np.mean(crimes_list)
crimes_range = (-crimes_std_percentage, crimes_std_percentage)

taxes = taxes_list [-1]
taxes_std_percentage = np.std(taxes_list [:-1])/np.mean(taxes_list)
taxes_range = (0, taxes_std_percentage)
