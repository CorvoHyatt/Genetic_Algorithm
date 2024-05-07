from typing import List


class SelectionOperator:
    def select(self, population: List[List[int]], num_parents: int) -> List[List[int]]:
        raise NotImplementedError("Método select debe ser implementado por subclases")
