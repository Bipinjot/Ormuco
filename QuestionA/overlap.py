def check_overlap(x1, y1, x2, y2):
    """
    Check if two line segments on the x-axis overlap.

    Args:
        x1, y1: Start and end points of the first line segment.
        x2, y2: Start and end points of the second line segment.

    Returns:
        True if the line segments overlap or touch, False otherwise.

    Raises:
        ValueError: If any of the input parameters are not numbers.
    """
    if not all(isinstance(coord, (int, float)) for coord in [x1, y1, x2, y2]):
        raise ValueError("All coordinates must be numbers.")
    
    if x1 <= x2 < y1 or x2 <= x1 < y2 or x1 < y2 <= y1 or x2 < y1 <= y2:
        return True
    return False
