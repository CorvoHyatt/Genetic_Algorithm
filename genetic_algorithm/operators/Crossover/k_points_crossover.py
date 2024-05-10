from typing import List
import numpy as np
from genetic_algorithm.Individuals.individual import Individual
from genetic_algorithm.operators.Crossover.crossover_operators import CrossoverOperator


class Kpoints(CrossoverOperator):
    @staticmethod
    def crossover(
        population_selected: List[Individual], k: int = 3
    ) -> List[Individual]:
        new_population = []
        for i in range(len(population_selected) - 1):
            parent1 = population_selected[i]
            parent2 = population_selected[i + 1]

            # Realizamos el crossover en k puntos
            crossover_points = sorted(
                np.random.choice(len(parent1.genotype) - 1, k, replace=False)
            )
            child_genotype = []
            start = 0
            for point in crossover_points:
                child_genotype.extend(parent1.genotype[start:point])
                parent1, parent2 = parent2, parent1
                start = point
            child_genotype.extend(parent1.genotype[start:])

            # Creamos un nuevo individuo con el genotipo resultante
            child = Individual(np.array(child_genotype))
            new_population.append(child)

        return new_population


# Crear instancias de Individual y asignarles un valor de fitness
individuals = []
for _ in range(6):
    genotype = np.random.randint(
        0, 2, size=(10,)
    )  # Ejemplo de un genotipo aleatorio de tamaño 10
    fitness_value = np.random.uniform(
        0, 1
    )  # Ejemplo de un valor de fitness aleatorio entre 0 y 1
    individual = Individual(genotype)
    individual.fitness = fitness_value
    individuals.append(individual)

population = Kpoints.crossover(individuals)
print(*map(lambda x: x.__dict__, population), sep="\n")
