from creation.res.sudoku.puzzle import create_puzzle, display
from creation.res.genetic.population import create_population, evaluate_population
from creation.res.genetic.fitness import fitness_sudoku

def genetic_algorithm(population, fitness_fn, ngen=100, pmut=0.1, crossover="onepoint", mutation="position" ): 
    evaluate_population(population=population, fitness_fn=fitness_fn)    
    
    
def genetic_search_sudoku(namefile,numInd=10, crossover="onepoint",tasa=0.5 ,mutattion ="position",maxGen=50):
    puzzle = create_puzzle(namefile)    
    population = create_population(puzzle=puzzle, num=numInd)     
    return genetic_algorithm(population,fitness_sudoku)
    


