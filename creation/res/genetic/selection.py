from random import randint,uniform

#ctjacobs
def compete(population): 
    size_pop = len(population) - 1
    gladiator1 = population[randint(0, size_pop)]
    gladiator2 = population[randint(0, size_pop)]

    f1 = gladiator1.fitness
    f2 = gladiator2.fitness

    fittest, weakest = (gladiator1, gladiator2) if f1 > f2 else  (gladiator2, gladiator1)

    selection_rate = 0.85    
    r = uniform(0,1)
    return fittest if r < selection_rate else weakest
    

def select_parents_tournament(population):
    parent1 = compete(population)
    parent2 = compete(population)    

    return (parent1, parent2)


def select_parents_roulette(population):
    """Seleccion por roulette, basado en el algoritmo nqueens"""
    popsize = len(population)
    
    # Seleccion del primer padre
    sumfitness = sum([individual.fitness for individual in population])  # suma total del fitness de la poblacion
    pickfitness = uniform(0, sumfitness)   
    cumfitness = 0     
    for i in range(popsize):
        cumfitness += population[i].fitness
        if cumfitness > pickfitness: 
            iParent1 = i
            break

    # Seleccion del segundo padre
    sumfitness = sumfitness - population[iParent1].fitness # retira el fitness del padre ya escogido
    pickfitness = uniform(0, sumfitness)   
    cumfitness = 0     
    for i in range(popsize):
        if i == iParent1: continue   # si es el primer padre 
        cumfitness += population[i].fitness
        if cumfitness > pickfitness: 
            iParent2 = i
            break        
    return (population[iParent1], population[iParent2])