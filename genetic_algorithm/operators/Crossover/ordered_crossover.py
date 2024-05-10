from typing import List

import numpy as np
from genetic_algorithm.Individuals.individual import Individual
from genetic_algorithm.operators.Crossover.crossover_operators import CrossoverOperator


class Ordered(CrossoverOperator):
    @staticmethod
    def crossover(population_selected: List[Individual]) -> List[Individual]:
        new_population = []
        for i in range(len(population_selected) - 1):
            parent1 = population_selected[i]
            parent2 = population_selected[i + 1]

            # Realizamos la cruza ordenada OX1
            start = np.random.randint(0, len(parent1.genotype))
            end = np.random.randint(start + 1, len(parent1.genotype))
            child_genotype = [-1] * len(parent1.genotype)
            child_genotype[start:end] = parent1.genotype[start:end]
            index = end
            for g in parent2.genotype[end:] + parent2.genotype[:end]:
                if g not in child_genotype:
                    child_genotype[index % len(parent1.genotype)] = g
                    index += 1

            # Creamos un nuevo individuo con el genotipo resultante
            child = Individual(np.array(child_genotype))
            new_population.append(child)

        return new_population


# Crear instancias de Individual y asignarles un valor de fitness
individuals = []
for _ in range(2):
    genotype = np.random.randint(
        0, 2, size=(10,)
    )  # Ejemplo de un genotipo aleatorio de tamaño 10
    fitness_value = np.random.uniform(
        0, 1
    )  # Ejemplo de un valor de fitness aleatorio entre 0 y 1
    individual = Individual(genotype)
    individual.fitness = fitness_value
    individuals.append(individual)

print(*map(lambda x: x.__dict__, individuals), sep="\n")
population = Ordered.crossover(individuals)
print(*map(lambda x: x.__dict__, population), sep="\n")
