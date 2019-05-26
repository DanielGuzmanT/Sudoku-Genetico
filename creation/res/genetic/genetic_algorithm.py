
from creation.res.sudoku.puzzle import create_puzzle, display
from creation.res.genetic.population import create_population, evaluate_population
from creation.res.genetic.fitness import fitness_sudoku
from creation.res.genetic.selection import select_parents_tournament, select_parents_roulette
from creation.res.genetic.survive import select_survivors

from creation.res.genetic.individual import Individual
from random import uniform
import time

def set_worst_ind(population, best_ind): 
    w_index = sorted(range(len(population)), key = lambda i: population[i].fitness)[0]
    population[w_index] = best_ind

def get_best_ind(population): 
    index = sorted(range(len(population)), key = lambda i: population[i].fitness, reverse = True)[0]
    return population[index]


def genetic_algorithm(population, invariants, numInd, ngen=100, pmut=0.1, crossover="onepoint", mutation="position", selection="tournament", fitness_fn=fitness_sudoku):  
    
    best_ind = get_best_ind(population)
    best_gen, n_pop_init = 0, len(population)
    
    print('Mejor individuo de la poblacion inicial\n')
    display(best_ind.chromosome)
    print('Fitness: {}'.format(best_ind.fitness))
    print('generacion: {}'.format(best_gen))
    
    start_time = time.time()

    for gen in range(ngen):
        mating_pool = [] 
        if selection == 'tournament':
            for _ in range(len(population) // 2): mating_pool.append(select_parents_tournament(population))
        elif selection == 'roulette':
            for _ in range(len(population) // 2): mating_pool.append(select_parents_roulette(population))
        
        if pmut == 1.0:
            offspring = population
        else:
            offspring = []
            # cruzamiento
            for parents in mating_pool:
                if(crossover == 'onepoint'):
                    offspring.extend(parents[0].crossover_single_point(parents[1]))
                elif(crossover == 'uniform'): 
                    offspring.extend(parents[0].crossover_uniform(parents[1]))
                elif(crossover == 'newcross'): 
                    offspring.extend(parents[0].crossover_new(parents[1]))
        # mutacion 
        for index in range(len(offspring)):
            if uniform(0, 1) < pmut: 
                if mutation == 'position':                    
                    offspring[index] = offspring[index].mutate_position(invariants) 
                elif mutation == 'swap': 
                    offspring[index] = offspring[index].mutate_swap(invariants)
                elif mutation == 'newswap': 
                    offspring[index] = offspring[index].mutate_new_swap(invariants)
                

        # evaluar offspring 
        evaluate_population(population=offspring, fitness_fn=fitness_fn)
        # seleccionar sobrevivientes
        population = select_survivors(population=population, offspring= offspring, numsurvivors= len(population))
        # se almacena el mejor individuo
        new_best_ind = get_best_ind(population)
        if new_best_ind.fitness > best_ind.fitness: 
            best_ind = new_best_ind
            best_gen = gen
        # si en la nueva poblacion no hay un individuo mejor
        else: 
            set_worst_ind(population, best_ind)

    end_time = time.time()

    print('\n\n')
    print('Mejor individuo de la poblacion final\n')
    display(best_ind.chromosome)
    print('Fitness: {}'.format(best_ind.fitness))
    print('Generacion: {}'.format(best_gen+1))
    n_calls = (best_gen+1) * numInd + n_pop_init
    print(f"Llamadas scoreboard: {n_calls}")

    print('\nTiempo: {}'.format(end_time-start_time))
    return best_ind

    
def genetic_sudoku(namefile, numInd, ngen=100, pmut=0.1, crossover="onepoint", mutation="position",selection="tournament"):
    puzzle = create_puzzle(namefile)
    invariants = [k for k,v in puzzle.items() if v != '0']
    print('Tablero inicial\n')
    display(puzzle)
    population = create_population(puzzle=puzzle,num=numInd)
    evaluate_population(population=population, fitness_fn=fitness_sudoku)
    return genetic_algorithm(population, invariants, numInd, ngen, pmut, crossover, mutation, selection)