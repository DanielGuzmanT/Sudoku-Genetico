from creation.res.sudoku.puzzle import create_puzzle, display
from creation.res.genetic.population import create_population, evaluate_population
from creation.res.genetic.fitness import fitness_sudoku
from creation.res.genetic.genetic_algorithm import genetic_search_sudoku


if __name__ == "__main__":
    genetic_search_sudoku(namefile="puzzleA.txt",numInd=10)


