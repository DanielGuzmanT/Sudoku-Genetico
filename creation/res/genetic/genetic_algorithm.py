
from creation.res.sudoku.puzzle import create_puzzle, display
from creation.res.genetic.population import create_population, evaluate_population
from creation.res.genetic.fitness import fitness_sudoku
from creation.res.genetic.selection import select_parents_tournament
from creation.res.genetic.survive import select_survivors

from creation.res.genetic.individual import Individual
from random import uniform

def genetic_algorithm(namefile, numInd, ngen=100, pmut=0.1, crossover="onepoint", mutation="position",fitness_fn=fitness_sudoku):  
    puzzle = create_puzzle(namefile)
    invariants = [k for k,v in puzzle.items() if v == '0']

    population = create_population(puzzle=puzzle, num=numInd)
    evaluate_population(population=population, fitness_fn=fitness_fn)   

    ####
    best_ind = sorted(range(len(population)), key = lambda i: population[i].fitness, reverse = True)[:1]

    print(best_ind)
    best_gen = 0
    print('Mejor individuo de la poblacion inicial\n')
    display(best_ind.chromosome)

    for gen in range(ngen):
        mating_pool = [] 
        for _ in range(len(population) / 2): mating_pool.append(select_parents_tournament(population))
        
        offspring = []
        # cruzamiento
        for parents in mating_pool:
            if(crossover == 'onepoint'):
                offspring.extend(parents[0].crossover_single_point(parents[1]))
        
        # mutacion -> realiza una copia o trabaja con la misma referencia?
        for individual in offspring:
            if uniform(0, 1) < pmut: 
                if mutation == "position":
                    individual = individual.mutate_position(invariants) 

        # evaluar offspring 
        evaluate_population(population=offspring, fitness_fn=fitness_fn)
        # seleccionar sobrevivientes
        population = select_survivors(population=population, offspring= offspring, numsurvivors= len(population))
        new_best_ind = sorted(range(len(population)), key = lambda i: population[i].fitness, reverse = True)[0]
        if(new_best_ind.fitness > best_ind): 
            best_ind = new_best_ind
            best_gen = gen
    
    print('Mejor individuo de la poblacion final\n')
    display(best_ind.chromosome)
    return best_ind

    


