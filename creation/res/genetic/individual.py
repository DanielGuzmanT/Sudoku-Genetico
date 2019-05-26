
from random import randrange,randint,uniform,sample
from ..sudoku.units import rows_units, cols_units, squares_units
from creation.res.genetic.fitness import fitness_peer

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

    def crossover_new(self,other_ind): 
        #basado en APLICACIÓN DE TÉCNICAS DE OPTIMIZACIÓN COMBINATORIAL
        chromosome1 = {}
        chromosome2 = {}
        # para el primer chromosoma se escogen los mejores squares
        for square in squares_units:
            if(fitness_peer(self.chromosome,square) > fitness_peer(other_ind.chromosome,square)): 
                for key in square: chromosome1[key] = self.chromosome[key]
            else: 
                for key in square: chromosome1[key] = other_ind.chromosome[key]
        
        # para el segundo los mejores rows o columns 
        if uniform(0,1) < 0.5: 
            for row in rows_units: 
                if(fitness_peer(self.chromosome,row) > fitness_peer(other_ind.chromosome,row)): 
                    for key in row: chromosome2[key] = self.chromosome[key]
                else: 
                    for key in row: chromosome2[key] = other_ind.chromosome[key]
        else: 
            for col in cols_units: 
                if(fitness_peer(self.chromosome,col) > fitness_peer(other_ind.chromosome,col)): 
                    for key in col: chromosome2[key] = self.chromosome[key]
                else: 
                    for key in col: chromosome2[key] = other_ind.chromosome[key]

        ind1 = Individual(chromosome1)
        ind2 = Individual(chromosome2)
        return [ind1, ind2] 

    def mutate_element(self, unit, invariants):
        mutated_ind = Individual(self.chromosome)
        index_gen  = randint(0, len(unit)-1)
        while True: 
            index_element = randint(0,8)
            keys_gen = unit[index_gen]
            if keys_gen[index_element] not in invariants:
                mutated_ind.chromosome[keys_gen[index_element]]=str(randint(1, 9))    
                return mutated_ind
    
    def mutate_position(self, invariants):
        prob = uniform(0,1)
        #rows 
        if prob <= 0.33:
            return self.mutate_element(rows_units,invariants)
        #column
        elif prob > 0.33 and prob <= 0.66:
           return self.mutate_element(cols_units,invariants)
        #block
        else: 
           return self.mutate_element(squares_units,invariants)

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


    def mutate_new_swap(self,unit,invariants): 
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

    
                
            
 
        

