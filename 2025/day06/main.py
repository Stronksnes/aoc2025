import argparse 
import os 
import re
import math

from common.helper import load_input, load_example

DAY = 6
YEAR = 2025
BASE_DIR = os.path.dirname(__file__) 

class colonizer:
    def __init__(self, lines):
        self.lines = lines
        self.cols = []
        self.cols_op = []

    def clean(self):
        row = 0
        for line in self.lines:
            line = re.sub(r"\s+", ",", line) 
            values = line.split(",")  
            
            col = 0
            
            for v in values:
                if col >= len(self.cols):
                    self.cols.append([])

                if v in "*+": 
                    self.cols_op.append(v)

                else:
                    self.cols[col].append(int(v))

                col += 1

            row += 1

    def sum(self):
        c = 0
        all = []
        for col in self.cols:
            if self.cols_op[c] == "+":
                all.append(sum(col))

            if self.cols_op[c] == "*":
                all.append(math.prod(col))

            c += 1

        return sum(all)

    def cepha_clean(self):
        cols = self.cols
        self.cols = []

        for col in cols:
            new_col = []

            for numbers in col:
                digits = list(reversed(str(numbers)))

                for i, d in enumerate(digits):
                    if i >= len(new_col):
                        new_col.append([])
                    new_col[i].append(d)

            for ci, row in enumerate(new_col):
                new_col[ci] = int("".join(row))

            self.cols.append(new_col)

def task01(lines):
    lines = lines.split("\n")
    lc = colonizer(lines)

    lc.clean()
    lc.sum()

    print(lc.cols)               
    print(lc.cols_op)

    return lc.sum()

def task02(lines):
    lines = lines.split("\n")
    lc = colonizer(lines)

    lc.clean()
    lc.cepha_clean()
    print(lc.cols)               
    
    return lc.sum()

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
