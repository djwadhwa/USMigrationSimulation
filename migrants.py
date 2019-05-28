#migrants:

class Migrants:
    age_dist = 0
    wealth_dist = 0
    population = 0
    def __init__ (self, population, age, wealth):
        self.population = population
        self.age_dist = age
        self.wealth_dist = wealth
        
m = Migrants(100, 20, 20)
print (m.wealth_dist)