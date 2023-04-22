def multi_compare(value: float, conditions: list[float]):
    for index, condition in enumerate(conditions):
        if value < condition:
            return index
