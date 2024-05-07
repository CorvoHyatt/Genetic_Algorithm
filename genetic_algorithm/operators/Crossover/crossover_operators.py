class CrossoverOperator:
    def crossover(self, parent1: list[int], parent2: list[int]) -> list[int]:
        raise NotImplementedError(
            "Método crossover debe ser implementado por subclases"
        )
