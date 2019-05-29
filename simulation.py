#simulation
import random as rnd
import Seattle as sea

deltaTime = 1
totalTime = 20

def age_dist(population, children, adults):
    randNum = rnd.uniform(-1,1)
    print(randNum)
    
#test    
for i in range (10):   
    age_dist(sea.population, sea.children, sea.adults)