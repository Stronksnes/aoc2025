import argparse 
import os 

from collections import defaultdict
from common.helper import load_input, load_example

DAY = 7
YEAR = 2025
BASE_DIR = os.path.dirname(__file__) 

class Manifold:
    def __init__(self, manifold, starter, splitter, empty, laser):
        self.manifold = [list(row) for row in manifold]
        self.starter = starter
        self.empty = empty
        self.splitter = splitter
        self.split_count = 0
        self.laser = laser
        self.beams = []
        self.visualize = False
    
    def start(self):
        si = (self.manifold[0]).index(self.starter)
        self.beams.append(Beam(1, si, "S"))

    def run_simulation(self):
        while any(b.direction != "STOPPED" for b in self.beams):
            if self.visualize:
                self.print_grid()
            self.step()

    def print_grid(self):
        for row in self.manifold:
            print("".join(row))
        print()

    def add_beams(self, beam):
        self.beams.append(beam)

    def step(self):
        for beam in list(self.beams):

            if beam.direction == "STOPPED":
                continue

            if beam.x + 1 >= len(self.manifold):
                beam.stop()
                continue

            else: 
                beam.move()

            if self.manifold[beam.x][beam.y] == self.empty:
                self.manifold[beam.x][beam.y] = self.laser

            elif self.manifold[beam.x][beam.y] == self.splitter:
                
                self.split_count += 1
                left_y = beam.y - 1
                right_y = beam.y + 1

                self.add_beams(Beam(beam.x, left_y, "S"))
                self.manifold[beam.x][left_y] = self.laser

                self.add_beams(Beam(beam.x, right_y, "S"))
                self.manifold[beam.x][right_y] = self.laser

                beam.stop()
                continue

            else:
                beam.stop()
                

class Beam:
    instance_count = 0

    def __init__(self, x, y, direction):
        Beam.instance_count += 1
        self.beam_length = 0
        self.x = x
        self.y = y
        self.direction = direction

    def stop(self):
        self.direction = "STOPPED"

    def move(self):
        if self.direction == "S":
            self.x += 1
            self.beam_length += 1


def task01(lines):
    print(lines)
    line_array = lines.split("\n")
    m = Manifold(line_array, "S", "^", ".", "|")
    m.visualize = True
    m.start()
    m.run_simulation()

    return m.split_count

"""
def task02(lines):
    print(lines)
    line_array = lines.split("\n")
    m = Manifold(line_array, "S", "^", ".", "|")
    m.visualize = True
    m.start()
    m.run_simulation()
    
    beam_c = len(m.beams)

    return beam_c
"""

def task02(lines):
    grid = [list(row) for row in lines.split("\n")]
    w = len(grid[0])
    h = len(grid)
    
    start = grid[0].index("S")

    states = {(1, start): 1}
    completed = 0

    while states:
        new_states = defaultdict(int)

        for (x, y), count in states.items():
            if x >= h - 1:
                completed += count
                continue

            tile = grid[x][y]

            if tile == ".":
                new_states[(x + 1, y)] += count

            elif tile == "^":
                left_y = y - 1
                right_y = y + 1
                new_states[(x, left_y)] += count
                new_states[(x, right_y)] += count

        states = new_states

    return completed


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
