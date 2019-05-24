
from random import randrange,randint,uniform
from ..sudoku.units import rows_units

class Individual:
    
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = -1

    def crossover_single_point(self, other_ind):
        point = randrange(len(self.chromosome))
        ind1 = Individual(self.chromosome[:point] + other_ind.chromosome[point:])
        ind2 = Individual(other_ind.chromosome[:point] + self.chromosome[point:])
        return [ind1, ind2]  

    def crossover_uniform(self):
        pass


    def mutate_position(self, invariants):
        mutated_ind = Individual(self.chromosome)
        index = randint(0, len(rows_units)-1)
        
        for key in rows_units[index]: 
            if key not in invariants:
                mutated_ind[key] = str(randint(1, 9))
                
        return mutated_ind


    def mutate_swap(self):
        pass
