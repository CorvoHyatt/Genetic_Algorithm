from typing import List
from random import sample

import numpy as np
from genetic_algorithm.Individuals.individual import Individual


class TournamentSelection:
    @staticmethod
    def select(population: List[Individual], tournament_size: int) -> List[Individual]:
        selected_parents = []
        while len(selected_parents) < len(population) + 1:
            # Seleccionar un subconjunto aleatorio de individuos para el torneo
            tournament = sample(population, tournament_size)
            # Seleccionar al individuo con el mejor fitness en el torneo
            winner = max(tournament, key=lambda x: x.fitness)
            # Verificar que el nuevo padre sea diferente de los padres seleccionados previamente
            if not selected_parents or winner != selected_parents[-1]:
                selected_parents.append(winner)
        return selected_parents


# Crear instancias de Individual y asignarles un valor de fitness
individuals = []
for _ in range(10):
    genotype = np.random.randint(
        0, 2, size=(10,)
    )  # Ejemplo de un genotipo aleatorio de tamaño 10
    fitness_value = np.random.uniform(
        0, 1
    )  # Ejemplo de un valor de fitness aleatorio entre 0 y 1
    individual = Individual(genotype)
    individual.fitness = fitness_value
    individuals.append(individual)

population = TournamentSelection.select(individuals, 3)
print(*map(lambda x: x.__dict__, population), sep="\n")
