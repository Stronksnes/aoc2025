import argparse 
import os 
import itertools

from common.helper import load_input, load_example

DAY = 9
YEAR = 2025
BASE_DIR = os.path.dirname(__file__) 

def task01(lines):
    input = lines.split("\n")
    rows = [(int(x), int(y)) for x, y in (line.split(",") for line in input)]

    print(rows)

    max_area = 0
    best_pair = None

    for (x1, y1), (x2, y2) in itertools.combinations(rows, 2):
        width = abs(x1 - x2) + 1
        height = abs(y1 - y2) + 1
        area = width * height

        if area > max_area:
            max_area = area
            best_pair = ((x1, y1), (x2, y2))

    print("Max area:", max_area)
    print("Pair:", best_pair)

    return max_area

def task02(lines):
    input = lines.split("\n")
    rows = [(int(x), int(y)) for x, y in (line.split(",") for line in input)]

    x_ranges = []
    y_ranges = []

    for (x1, y1), (x2, y2) in itertools.combinations(rows, 2):
        x_start, x_end = sorted([x1, x2])
        y_start, y_end = sorted([y1, y2])

        x_ranges.append((x_start, x_end))
        y_ranges.append((y_start, y_end))

        max_area = 0
        best_pair = None

        for (x1, y1), (x2, y2) in itertools.combinations(rows, 2):
            
            x_start, x_end = sorted([x1, x2])
            y_start, y_end = sorted([y1, y2])

            width = x_end - x_start + 1
            height = y_end - y_start + 1
            area = width * height

            if (x_start, x_end) in x_ranges and (y_start, y_end) in y_ranges:
                if area > max_area:
                    max_area = area
                    best_pair = ((x1, y1), (x2, y2))

        print("Max area:", max_area)
        print("Pair:", best_pair)

        return max_area

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", type=str, default="all", help="1 | 2")
    parser.add_argument("--example", action="store_true")
    parser.add_argument("--visualize", action="store_true")
    parser.add_argument("--force", action="store_true")

    args = parser.parse_args()

    if(args.example):
        lines = load_example(DAY, YEAR, BASE_DIR, force=args.force)
    else:
        lines = load_input(DAY, YEAR, BASE_DIR, force=args.force)

    result = None

    if args.task == "1":
        result = task01(lines)

    elif args.task == "2":
        result = task02(lines)
        
    print(result)


if __name__ == "__main__":
    main()
