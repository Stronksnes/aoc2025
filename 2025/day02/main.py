import argparse
import os
import re

from common.helper import load_input, load_example

DAY = 2
YEAR = 2025
BASE_DIR = os.path.dirname(__file__) 

def task01(lines):
    lines = lines.split(',')
    output = []
    for line in lines:
        start_str, end_str = line.split('-')
        start = int(start_str)
        end = int(end_str)

        r = range(start, end + 1)

        for lr in list(r):
            lr_str = str(lr)
            
            l = len(lr_str)
            is_even = (l % 2 == 0)

            if(is_even):
                split1 = lr_str[0:(l//2)]
                split2 = lr_str[(l//2):l]

                if(split1 == split2):
                    output.append(lr)    
                    print(f"invalid: {lr_str}")       

            else:
                print(f"valid: {lr_str}")

    print (output)
    return sum(output)            

def task02(lines):
    lines = lines.split(',')
    output = []
    for line in lines:
        start_str, end_str = line.split('-')
        start = int(start_str)
        end = int(end_str)

        r = range(start, end + 1)
        for lr in list(r):
            lr_str = str(lr)
            
            is_match = bool(re.match(r"^(.+?)\1+$", lr_str))
            if(is_match):
                print(f"invalid: {lr_str}")
                output.append(lr)
            else:
                print(f"valid: {lr_str}")
            
    print(output)
    return sum(output)

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
