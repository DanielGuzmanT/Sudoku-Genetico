
from creation.res.sudoku.puzzle import create_puzzle, display
from creation.res.genetic.population import create_population, evaluate_population
from creation.res.genetic.fitness import fitness_sudoku
from creation.res.genetic.selection import select_parents_tournament
from creation.res.genetic.survive import select_survivors

from creation.res.genetic.individual import Individual
from random import uniform
import time

def get_best_ind(population): 
    index = sorted(range(len(population)), key = lambda i: population[i].fitness, reverse = True)[0]
    return population[index]


def genetic_algorithm(population, invariants, numInd, ngen=100, pmut=0.1, crossover="onepoint", mutation="position",fitness_fn=fitness_sudoku):  
  
    best_ind = get_best_ind(population)    
    best_gen = 0
    
    print('Mejor individuo de la poblacion inicial\n')
    display(best_ind.chromosome)
    print('Fitness: {}'.format(best_ind.fitness))
    print('generacion: {}'.format(best_gen))
    
    start_time = time.time()

    for gen in range(ngen):
        mating_pool = [] 
        for _ in range(len(population) // 2): mating_pool.append(select_parents_tournament(population))
        
        offspring = []
        # cruzamiento
        for parents in mating_pool:
            if(crossover == 'onepoint'):
                offspring.extend(parents[0].crossover_single_point(parents[1]))
            if(crossover == 'uniform'): 
                offspring.extend(parents[0].crossover_uniform(parents[1]))
        # mutacion 
        for index in range(len(offspring)):
            if uniform(0, 1) < pmut: 
                if mutation == 'position':                    
                    offspring[index] = offspring[index].mutate_position(invariants) 
                if mutation == 'swap': 
                    offspring[index] = offspring[index].mutate_swap(invariants)
        # evaluar offspring 
        evaluate_population(population=offspring, fitness_fn=fitness_fn)
        # seleccionar sobrevivientes
        population = select_survivors(population=population, offspring= offspring, numsurvivors= len(population))
        
        new_best_ind = get_best_ind(population)
        if new_best_ind.fitness > best_ind.fitness: 
            best_ind = new_best_ind
            best_gen = gen
    
    end_time = time.time()

    print('\n\n')
    print('Mejor individuo de la poblacion final\n')
    display(best_ind.chromosome)
    print('Fitness: {}'.format(best_ind.fitness))
    print('Generacion: {}'.format(best_gen))
    
    print('\nTiempo: {}'.format(end_time-start_time))
    return best_ind

    
def genetic_sudoku(namefile, numInd, ngen=100, pmut=0.1, crossover="onepoint", mutation="position"):
    puzzle = create_puzzle(namefile)
    invariants = [k for k,v in puzzle.items() if v != '0']
    print('Tablero inicial\n')
    display(puzzle)
    population = create_population(puzzle=puzzle,num=numInd)
    evaluate_population(population=population, fitness_fn=fitness_sudoku)
    return genetic_algorithm(population, invariants, numInd, ngen, pmut, crossover, mutation)