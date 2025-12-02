import os
from aocd.models import Puzzle


def ensure_dir(base_dir: str) -> str:
    os.makedirs(base_dir, exist_ok=True)
    return base_dir


def load_input(day: int, year: int, base_dir: str, force: bool = False) -> str:
    base_dir = ensure_dir(base_dir)
    file_path = os.path.join(base_dir, "input.txt")

    if os.path.exists(file_path) and not force:
        with open(file_path) as f:
            return f.read()

    puzzle = Puzzle(year=year, day=day)
    input_data = puzzle.input_data

    with open(file_path, "w") as f:
        f.write(input_data)

    return input_data


def load_example(day: int, year: int, base_dir: str, force: bool = False) -> str:
    base_dir = ensure_dir(base_dir)
    file_path = os.path.join(base_dir, "example.txt")

    if os.path.exists(file_path) and not force:
        with open(file_path) as f:
            return f.read()

    puzzle = Puzzle(year=year, day=day)

    if not puzzle.examples:
        raise ValueError(f"No examples found for {year} day {day}")

    example_data = puzzle.examples[0].input_data

    with open(file_path, "w") as f:
        f.write(example_data)

    return example_data

