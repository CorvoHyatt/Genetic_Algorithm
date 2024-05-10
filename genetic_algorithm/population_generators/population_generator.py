from typing import List

from genetic_algorithm.Individuals.individual import Individual


class PopulationGenerator:
    @staticmethod
    def generate_population() -> List[Individual]:
        raise NotImplementedError("Método select debe ser implementado por subclases")
