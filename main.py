from creation.res.sudoku.puzzle import create_puzzle, display
from creation.res.genetic.population import create_population

if __name__ == "__main__":
    puzzle = create_puzzle('puzzleA.txt')    
    population = create_population(puzzle=puzzle, num=5)
    display(puzzle)
