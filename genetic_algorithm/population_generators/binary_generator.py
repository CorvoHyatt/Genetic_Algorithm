import pprint
from typing import List
import numpy as np

from ..Individuals.individual import Individual


class BinaryPopulationGenerator:

    @staticmethod
    def generate_population(self, population_size: int, genotype_structure: List[int]):
        bits_enteros, bits_decimales, variables = genotype_structure
        population = []
        for _ in range(population_size):
            genotype = np.random.choice(
                [0, 1],
                size=(bits_enteros + bits_decimales + 1) * variables,
            )
            individual = Individual(genotype)
            population.append(individual)

        return population


population = BinaryPopulationGenerator.generate_population(10, [2, 3, 2])
pprint.pprint(population)
