
from copy import deepcopy
from .individual import Individual
from random import randint

def create_population(puzzle, num=10):
    chromosomes = [deepcopy(puzzle) for i in range(num)]
    invariants  = [k for k,v in puzzle.items() if v=='0']

    for chromo in chromosomes:
        for ind in invariants:
            chromo[ind] = str(randint(1, 9))

    return [Individual(chromo) for chromo in chromosomes]


def evaluate_population(population, fitness_fn):
    for individual in population:
        if individual.fitness == -1:    # si el individuo no esta evaluado
            individual.fitness = fitness_fn(individual.chromosome)
    