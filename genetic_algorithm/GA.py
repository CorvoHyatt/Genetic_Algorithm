from typing import List, Literal
from genetic_algorithm.Individuals.individual import Individual
from genetic_algorithm.operators.Crossover.crossover_operators import CrossoverOperator
from genetic_algorithm.operators.Mutation.mutation_operators import MutationOperator
from genetic_algorithm.operators.Selection.selection_operators import SelectionOperator
from genetic_algorithm.population_generators.population_generator import (
    PopulationGenerator,
)


class GeneticAlgorithm:
    def __init__(
        self,
        selection_operator: SelectionOperator,
        crossover_operator: CrossoverOperator,
        mutation_operator: MutationOperator,
        population_size: int = 100,
        probability_mutation: int = 2,
        codification: Literal[
            "binary", "permutation", "combination", "real"
        ] = "permutation",
    ):
        self.population_size = population_size
        self.selection_operator = selection_operator
        self.crossover_operator = crossover_operator
        self.mutation_operator = mutation_operator
        if codification == ""
			self.population_generator = population_generator

    def initialize_population(self) -> List[Individual]:
        # Lógica para inicializar la población
        return self.population_generator.generate_population(self.population_size)

    def select_parents(self, population: List[Individual]) -> List[Individual]:
        # Lógica para seleccionar padres
        return self.selection_operator.select(population)

    def crossover(self, population: List[Individual]) -> List[Individual]:
        # Lógica para realizar el cruce
        return self.crossover_operator.crossover()

    def mutate(self, population: List[Individual]) -> List[Individual]:
        # Lógica para realizar la mutación
        return self.mutation_operator.mutate(population)

    def evolve(
        self,
    ) -> List[Individual]:
        parents = self.select_parents(population)
