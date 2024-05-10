from typing import List, Literal
from genetic_algorithm.Individuals.individual import Individual
from genetic_algorithm.operators.Crossover.crossover_operators import CrossoverOperator
from genetic_algorithm.operators.Mutation.mutation_operators import MutationOperator
from genetic_algorithm.operators.Selection.selection_operators import SelectionOperator
from genetic_algorithm.population_generators.binary_generator import (
    BinaryPopulationGenerator,
)
from genetic_algorithm.population_generators.comninatory_generator import (
    CombinatoryPopulationGenerator,
)
from genetic_algorithm.population_generators.permutation_generator import (
    PermutationPopulationGenerator,
)
from genetic_algorithm.population_generators.population_generator import (
    PopulationGenerator,
)
from genetic_algorithm.utils.utils import calcular_promedio_fitness


class GeneticAlgorithm:
    def __init__(
        self,
        selection_operator: SelectionOperator,
        crossover_operator: CrossoverOperator,
        mutation_operator: MutationOperator,
        stopping_criteria_type: Literal[
            "function_calls", "iterations", "found_optimal", "nochangebest"
        ] = "nochangebest",
        max_call_functions: int = None,
        max_iterations: int = None,
        optimal_solution: int = None,
        max_nochange_best: int = None,
        long_term_memory_reset: bool = True,
        problem_type: Literal["COP", "BenchMark"] = "BenchMark",
        limits: tuple[int, int] = [0, 32],
        population_size: int = 100,
        probability_mutation: int = 7,
        codification: Literal[
            "binary", "permutation", "combination", "real"
        ] = "permutation",
    ):
        self.population_size = population_size
        self.selection_operator = selection_operator
        self.crossover_operator = crossover_operator
        self.mutation_operator = mutation_operator
        self.probability_mutation = probability_mutation
        self.stopping_criteria_type = stopping_criteria_type
        self.max_call_functions = max_call_functions
        self.max_iterations = max_iterations
        self.optimal_solution = optimal_solution
        self.max_nochange_best = max_nochange_best
        self.long_term_memory_reset = long_term_memory_reset
        self.problem_type = problem_type
        self.limits = limits
        if codification == "binary":
            self.population_generator = BinaryPopulationGenerator
        elif codification == "permutation":
            self.population_generator = PermutationPopulationGenerator
        else:
            self.population_generator = CombinatoryPopulationGenerator

    def _clear(self, objetive):
        self._cost_worst = []
        self._cost_best = []
        self._cost_prom = []
        self.actual_best = None
        self.iterations = 0
        self.best_nochange_conunter = 0
        self.function_call_counter = 0
        self.objetive = objetive
        self.actual_solution_value = self.best
        self.function_call_counter += 1
        self._cost_best.append(self.best)

    def update_costs(self, population: List[Individual]):
        best = (min if self.min_or_max == "min" else max)(
            population, key=lambda individual: individual.fitness
        )
        self._cost_best.append(best)
        worst = (max if self.min_or_max == "min" else min)(
            population, key=lambda individual: individual.fitness
        )
        self._cost_worst.append(worst)
        prom = calcular_promedio_fitness(population)
        self._cost_prom.append(prom)

    def stopping_criteria(self) -> bool:
        if (
            self.stopping_criteria_type == "nochangebest"
            and self.best_nochange_conunter > self.max_nochange_best
        ):
            return False

        if (
            self.stopping_criteria_type == "function_calls"
            and self.function_call_counter <= self.max_call_functions
        ):
            return False
        if (
            self.stopping_criteria_type == "iterations"
            and self.iterations > self.max_iterations
        ):
            return False

        if (
            self.stopping_criteria_type == "found_optimal"
            and self.best == self.optimal_solution
        ):
            return False

        return True

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

    def evolve(self, objetive) -> List[Individual]:
        self._clear(objetive)
        population = self.initialize_population()

        while self.stopping_criteria():
            population_selected = self.select_parents(population)
            population_cross = self.crossover_operator(population_selected)
            population = self.mutate(population_cross)
            self.update_costs(population)
