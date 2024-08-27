def max_of_two(x: int, y: int) -> int:
    """Given x and y, that are 2 numbers, return the biggest number."""
    biggest = x
    if x >= y:
        return biggest
    else:
        biggest = y
        return biggest

# Replace the "ANSWER HERE" for your answer
def max_of_three(x: int, y: int, z: int) -> int:
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    biggest = max_of_two(x,y)
    if z < (biggest):
        return biggest
    else:
        return z
