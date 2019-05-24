
def select_survivors(population, offspring, numsurvivors):
    survivors = sorted(range(len(population)), key = lambda i: population[i].fitness, reverse = True)[:numsurvivors]
    return survivors
