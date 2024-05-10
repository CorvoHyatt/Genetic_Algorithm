from typing import List
from genetic_algorithm.Individuals.individual import Individual
from genetic_algorithm.operators.Crossover.crossover_operators import CrossoverOperator
from genetic_algorithm.operators.Mutation.mutation_operators import MutationOperator
from genetic_algorithm.operators.Selection.selection_operators import SelectionOperator


class GeneticAlgorithm:
    def __init__(
        self,
        population_size: int,
        selection_operator: SelectionOperator,
        crossover_operator: CrossoverOperator,
        mutation_operator: MutationOperator,
    ):
        self.population_size = population_size
        self.selection_operator = selection_operator
        self.crossover_operator = crossover_operator
        self.mutation_operator = mutation_operator

    def initialize_population(self) -> List[Individual]:
        # Lógica para inicializar la población
        pass

    def select_parents(self, population: List[Individual]) -> List[Individual]:
        # Lógica para seleccionar padres
        return self.selection_operator.select(population)

    def crossover(self, population: List[Individual]) -> List[Individual]:
        # Lógica para realizar el cruce
        return self.crossover_operator.crossover()

    def mutate(self, population: List[Individual]) -> List[Individual]:
        # Lógica para realizar la mutación
        return self.mutation_operator.mutate(population)

    def evolve(self, population: List[Individual]) -> List[Individual]:
        parents = self.select_parents(population)
        offspring = []
        for i in range(0, len(parents), 2):
            child1, child2 = self.crossover(parents[i], parents[i + 1])
            offspring.append(self.mutate(child1))
            offspring.append(self.mutate(child2))
        return offspring
