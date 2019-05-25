
from random import randrange,randint,uniform,sample
from ..sudoku.units import rows_units, cols_units, squares_units

class Individual:
    
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = -1

    def crossover_single_point(self, other_ind):
        point = randrange(len(self.chromosome))
        chromo1_list = sorted(self.chromosome.items())
        chromo2_list = sorted(other_ind.chromosome.items())
        
        ind1 = Individual(dict(chromo1_list[:point] + chromo2_list[point:]))
        ind2 = Individual(dict(chromo2_list[:point] + chromo1_list[point:]))
        return [ind1, ind2]  

    def crossover_uniform(self, other_ind):
        chromosome1 = {}
        chromosome2 = {}

        for row in rows_units: 
            if uniform(0,1) < 0.5: 
                for k in row: 
                    chromosome1[k] = self.chromosome[k]
                    chromosome2[k] = other_ind.chromosome[k]
            else:
                for k in row: 
                    chromosome1[k] = other_ind.chromosome[k]
                    chromosome2[k] = self.chromosome[k]

        ind1 = Individual(chromosome1)
        ind2 = Individual(chromosome2)
        return [ind1, ind2] 


    def mutate_position(self, invariants):
        mutated_ind = Individual(self.chromosome)
        index = randint(0, len(rows_units)-1)
        
        for key in rows_units[index]: 
            if key not in invariants:
                mutated_ind.chromosome[key] = str(randint(1, 9))                
        
        return mutated_ind

    def mutate_swap(self, invariants):
        mutated_ind = Individual(self.chromosome)
        
        row_indx_1,row_indx_2 = sample(range(9),2)

        row1 = rows_units[row_indx_1]
        row2 = rows_units[row_indx_2]
        for i in range(9): 
            if row1[i] not in invariants and row2[i] not in invariants:
                mutated_ind.chromosome[row1[i]], mutated_ind.chromosome[row2[i]] = mutated_ind.chromosome[row2[i]], mutated_ind.chromosome[row1[i]]      
        return mutated_ind


    def swap_block(self, unit, invariants): 
        mutated_ind = Individual(self.chromosome)
        index_gen  = randint(0,8)
        keys_gen = unit[index_gen]
        while True: 
            sw_indx_1, sw_indx_2 = sample(range(9),2)
            if keys_gen[sw_indx_1] not in invariants and keys_gen[sw_indx_2] not in invariants:
                mutated_ind.chromosome[keys_gen[sw_indx_1]],mutated_ind.chromosome[keys_gen[sw_indx_2]] = mutated_ind.chromosome[keys_gen[sw_indx_2]],mutated_ind.chromosome[keys_gen[sw_indx_1]]
                return mutated_ind 


    def mutate_new_swap(self,invariants): 
        prob = uniform(0,1)
        #rows 
        if prob <= 0.33:
            return self.swap_block(rows_units,invariants)
        #column
        elif prob > 0.33 and prob <= 0.66: 
            return self.swap_block(cols_units,invariants)
        #block
        else: 
            return self.swap_block(squares_units,invariants)

        

