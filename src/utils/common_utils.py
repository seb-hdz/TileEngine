def multi_compare(value: float, conditions: list[float]) -> int or None:
    """
    Returns the index of the first element in the `conditions` list that the `value` is less than.
    
    Args:
    - value: A float representing the value to be compared against the `conditions`.
    - conditions: A list of floats representing the threshold values to be compared against the `value`.
    
    Returns:
    - If the `value` is less than an element in the `conditions` list, returns the index of that element.
    - If the `value` is greater than or equal to all elements in the `conditions` list, returns None.
    """
    for index, condition in enumerate(conditions):
        if value < condition:
            return index
    return None
