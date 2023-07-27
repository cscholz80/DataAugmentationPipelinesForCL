def extract_primary(filename: str) -> str:
    """
    Extracts the primary part of the filename before the first '/' character.

    Args:
        filename (str): The input filename from which the primary part needs to be extracted.

    Returns:
        str: The primary part of the filename.

    Raises:
        ValueError: If the input filename does not contain any '/' character.
    """

    # Find the position of the first '/' character in the filename
    pos = filename.find("/")

    if pos == -1:
        # If no '/' character is found, raise a ValueError
        raise ValueError("Input filename must contain a '/' character.")

    # Extract and return the primary part of the filename before the first '/'
    return filename[:pos]
