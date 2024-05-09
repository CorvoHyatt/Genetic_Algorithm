import numpy as np

from genetic_algorithm.Individuals.individual import Individual


class CombinatoryPopulationGenerator:
    @staticmethod
    def generate_population(population_size: int, limits: int):
        population = set()
        while len(population) < population_size:
            genotype = np.random.randint(1, limits + 1, size=limits)
            individual = Individual(genotype)
            population.add(individual)
