from ..sudoku.units import unitlist

def fitness_sudoku(chromosome):
    fit = 0  # best case: fit = 81 + 81 + 81 
    for unit in unitlist:  # rows units, cols units, squares units
        values = [chromosome[ind] for ind in unit]
        fit += len(set(values))

    return fit
