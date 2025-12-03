import argparse
import os
import re

from common.helper import load_input, load_example

DAY = 3
YEAR = 2025
BASE_DIR = os.path.dirname(__file__) 

class batterybank:
    def __init__(self, seq, do_sum=True):
        self.seq = seq
        self.array = [int(x) for x in seq]
        self.peaks = []
        self.max_val = 0
        self.find_peaks()
        self.battery_sum = 0

        if do_sum:
            self.find_battery_sum()

    def find_peaks(self):
        self.max_val = max(self.array)

        self.peaks = []
        for i, v in enumerate(self.array):
            if v == self.max_val:
                self.peaks.append({"index": i, "value": v})

        return self.peaks

    def find_battery_sum(self):
        values = []

        for peak in self.peaks:
            start_index = peak["index"]
            tail = self.seq[start_index + 1:]

            if tail:
                bb = batterybank(tail, do_sum=False)
                values.append(int(str(self.max_val) + str(bb.max_val)))
            else:
                head = self.seq[:start_index]
                if not head:
                    continue

                bb = batterybank(head, do_sum=False)
                values.append(int(str(bb.max_val) + str(self.max_val)))

        if values:
            self.battery_sum = max(values)
        else:
            self.battery_sum = self.max_val


def task01(lines):
    lines = lines.split('\n')
    output = [] 
    for line in lines:
        bb = batterybank(line)

        print(f"seq: {bb.seq}")
        print(f"peaks: {bb.peaks}")
        print(f"max_val: {bb.max_val}")
        print(f"battery_sum: {bb.battery_sum}")

        output.append(bb.battery_sum)

    return sum(output)

def task02(lines):
    pass

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
