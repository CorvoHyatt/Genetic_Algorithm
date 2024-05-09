import pprint
from genetic_algorithm.population_generators.binary_generator import (
    BinaryPopulationGenerator,
)

population = BinaryPopulationGenerator.generate_population(10, [2, 3, 2])
pprint.pprint(population)
