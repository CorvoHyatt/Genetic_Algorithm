from typing import List
from random import uniform
from genetic_algorithm.Individuals.individual import Individual


class StochasticUniversalSampling:
    @staticmethod
    def select(population: List[Individual]) -> List[Individual]:
        # Obtener los valores de aptitud de la población
        fitness_values = [individual.fitness for individual in population]

        # Calcular la suma total de aptitudes y el espacio de selección
        total_fitness = sum(fitness_values)
        selection_space = total_fitness / len(population)

        # Generar puntos de muestreo
        start = uniform(0, selection_space)
        points = [start + i * selection_space for i in range(len(population))]

        # Seleccionar padres basados en los puntos de muestreo
        selected_parents = []
        current_index = 0
        current_accumulated_fitness = fitness_values[0]
        while len(selected_parents) < len(population):
            while current_accumulated_fitness < points[len(selected_parents)]:
                current_index += 1
                current_accumulated_fitness += fitness_values[current_index]
            selected_parents.append(population[current_index])

        return selected_parents
