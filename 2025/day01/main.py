import argparse
import os

from common.helper import load_input, load_example
from common.round import circle


DAY = 1
YEAR = 2025
BASE_DIR = os.path.dirname(__file__) 

def task01(lines):

    c = circle(starterValue=50, maxValue=99, minValue=0)
    zC = 0

    for line in lines:
        direction = line[0]
        amount = int(line[1:])
            
        if direction == "R":
            c.increase(amount)
        elif direction == "L":
            c.decrease(amount)
    
        print(f"Current value: {c.value}")
        
        if(c.value == 0):
            zC = zC + 1

    return zC


def task02(lines):
    
    c = circle(starterValue=50, maxValue=99, minValue=0)

    for line in lines:
        direction = line[0]
        amount = int(line[1:])
            
        if direction == "R":
            c.increase(amount)
        elif direction == "L":
            c.decrease(amount)
    
    return c.wrapcounter


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
