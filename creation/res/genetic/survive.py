
def select_survivors(population, offspring, numsurvivors):
    next_generation=[]
    survivors = sorted(range(len(population)), key = lambda i: population[i].fitness, reverse = True)[:numsurvivors]
    for i in range(numsurvivors): next_generation.append(population[survivors[i]])
    return next_generation
