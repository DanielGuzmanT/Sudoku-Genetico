from random import randint,uniform

#ctjacobs
def compete(population): 
    size_pop = len(population)
    gladiator1 = population[randint(0, size_pop)]
    gladiator2 = population[randint(0, size_pop)]

    f1 = gladiator1.fitness
    f2 = gladiator2.fitness

    fittest, weakest = gladiator1, gladiator2 if f1 > f2 else  gladiator2, gladiator1

    selection_rate = 0.85    
    r = uniform(0,1)
    return fittest if r > selection_rate else weakest
    


def select_parents_tournament(population):
    parent1 = compete(population)
    parent2 = compete(population)    

    return (parent1, parent2)