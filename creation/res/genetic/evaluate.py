
def evaluate_population(population, fitness_fn):
    # TODO(1): cambiar todos los comentarios a inglés
    """ Evalua una poblacion de individuos con la funcion de fitness pasada """
    for individual in population:
        if individual.fitness == -1:    # si el individuo no esta evaluado
            individual.fitness = fitness_fn(individual.chromosome)
    