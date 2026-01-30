def print_star_pattern(rows: int = 5) -> None:
    """Print a star pattern with the given number of rows."""
    for row in range(1, rows + 1):
        print("*" * row)


if __name__ == "__main__":
    print_star_pattern()
