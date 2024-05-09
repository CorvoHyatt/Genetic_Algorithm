from typing import List
from random import choices

from genetic_algorithm.Individuals.individual import Individual


class RankSelection:
    @staticmethod
    def select(self, population: List[Individual]) -> List[Individual]:
        # Ordenar la población por aptitud de manera ascendente
        sorted_population = sorted(population, key=lambda x: x.fitness)

        # Calcular el rango de cada individuo
        ranks = list(range(1, len(sorted_population) + 1))

        # Calcular la probabilidad de selección para cada individuo basada en su rango
        total_ranks = sum(ranks)
        selection_probabilities = [rank / total_ranks for rank in ranks]

        # Seleccionar n+1 individuos usando la probabilidad de selección
        selected_parents = []
        while len(selected_parents) < len(population) + 1:
            new_parent = choices(
                sorted_population, weights=selection_probabilities, k=1
            )[0]
            if not selected_parents or new_parent != selected_parents[-1]:
                selected_parents.append(new_parent)

        return selected_parents
