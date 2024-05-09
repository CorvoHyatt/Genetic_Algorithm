# roulette_selection.py

from typing import List
from random import choices
from genetic_algorithm.Individuals.individual import Individual
from genetic_algorithm.operators.Selection.selection_operators import SelectionOperator


class RouletteSelection:
    @staticmethod
    def select(population: List[Individual], num_parents: int) -> List[Individual]:
        # Obtener los valores de aptitud de la población
        fitness_values = [individual.fitness for individual in population]

        # Seleccionar padres usando selección por ruleta
        selected_parents = []
        while len(selected_parents) < num_parents:
            new_parent = choices(population, weights=fitness_values, k=1)[0]
            if not selected_parents or new_parent != selected_parents[-1]:
                selected_parents.append(new_parent)

        return selected_parents
