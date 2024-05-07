from operators.Selection.selection_operators import SelectionOperator


class RouletteWheelSelection(SelectionOperator):
    def select(
        self, population: List[Individual], num_parents: int
    ) -> List[Individual]:
        # Implementación de la selección por ruleta
        fitness_values = [individual.fitness for individual in population]
        selected_parents = choices(population, weights=fitness_values, k=num_parents)
        return selected_parents
