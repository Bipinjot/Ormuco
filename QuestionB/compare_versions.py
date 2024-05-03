def compare_versions(version1, version2):
    """
    Compare two version strings and determine their relationship.

    Args:
        version1: First version string.
        version2: Second version string.

    Returns:
        1 if version1 > version2
        -1 if version1 < version2
        0 if version1 == version2
    """
    if not (isinstance(version1, str) and isinstance(version2, str)):
        raise TypeError("Inputs must be strings")

    # Check for invalid version format
    if not all(part.isdigit() for part in version1.split('.')) or \
            not all(part.isdigit() for part in version2.split('.')):
        raise ValueError("Invalid version format")

    v1_parts = [int(part) for part in version1.split('.')]
    v2_parts = [int(part) for part in version2.split('.')]

    # Pad the shorter version string with zeros to match the length of the longer one
    max_length = max(len(v1_parts), len(v2_parts))
    v1_parts.extend([0] * (max_length - len(v1_parts)))
    v2_parts.extend([0] * (max_length - len(v2_parts)))

    for v1, v2 in zip(v1_parts, v2_parts):
        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1

    return 0  # Both version strings are equal
