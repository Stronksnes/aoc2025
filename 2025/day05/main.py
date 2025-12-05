import argparse
import os

from common.helper import load_input, load_example

DAY = 5
YEAR = 2025
BASE_DIR = os.path.dirname(__file__) 

class range_coalescer:
    def __init__(self):
        self.ranges_c = []

    def absorb_range(self, r):
        rs = r.start
        re = r.stop - 1

        merged_start = rs
        merged_end = re

        new_list = []

        for c in self.ranges_c:
            cs = c.start
            ce = c.stop - 1

            if merged_end < cs - 1 or merged_start > ce + 1:
                new_list.append(c)
            else:
                merged_start = min(merged_start, cs)
                merged_end = max(merged_end, ce)

        new_list.append(range(merged_start, merged_end + 1))
        new_list.sort(key=lambda x: x.start)
        self.ranges_c = new_list
        print(self.ranges_c)

def task01(lines):
    ranges_str, input = lines.split("\n\n") 
   
    ranges_str = ranges_str.split("\n")
    input = list(map(int, input.split("\n")))

    ranges = []

    for r_str in ranges_str:
        start, end = map(int, r_str.split("-"))
        ranges.append(range(start, end + 1))
    
    fresh_c = 0
    for i in input:
        for r in ranges:
            if i in r:
                print(f"{i} fresh!")
                fresh_c += 1
                break

    return fresh_c

def task02(lines):
    ranges_str, null = lines.split("\n\n") 
   
    ranges_str = ranges_str.split("\n")

    rc = range_coalescer()

    ranges = []
    for r_str in ranges_str:
        start, end = map(int, r_str.split("-"))
        ranges.append(range(start, end + 1))

    for r in ranges:
        rc.absorb_range(r) 

    values = []
    for ranges_all in rc.ranges_c:
        values.append(len(ranges_all))

    return sum(values)

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
