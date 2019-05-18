from creation.res.sudoku.puzzle import create_puzzle, display
from creation.res.genetic.population import create_population, evaluate_population
from creation.res.genetic.fitness import fitness_sudoku

if __name__ == "__main__":
    puzzle = create_puzzle('puzzleA.txt')    
    display(puzzle)

    population = create_population(puzzle=puzzle, num=5)    
    evaluate_population(population=population, fitness_fn=fitness_sudoku)
    
    individual = population[0]
    display(individual.chromosome)
    print("="*200)
    print("fitness:", individual.fitness)
