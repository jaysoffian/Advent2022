#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/14
"""
import subprocess
import time
from collections import namedtuple
from pathlib import Path

import matplotlib.pyplot as plt
import typer
from celluloid import Camera

HERE = Path(__file__).parent
SAMPLE = (HERE / "sample.txt").read_text().strip().splitlines()
INPUT = (HERE / "input.txt").read_text().strip().splitlines()


def ansi_clear():
    print("\033[2J\033[1;1H", end="")


def ansi_home():
    print("\033[0;01H", end="")


def ordered(i, j):
    return (i, j) if i <= j else (j, i)


Coord = namedtuple("Coord", "x y")


class Board:
    @classmethod
    def from_input(cls, lines):
        board = cls()
        for line in lines:
            coords = line.split(" -> ")
            for c1, c2 in zip(coords, coords[1:]):
                board.add_line(c1, c2)
        return board

    def __init__(self):
        self.board = {}
        self.min_x = self.max_x = 500
        self.min_y = self.max_y = 0
        self[500, 0] = "+"

    def __setitem__(self, coord, item):
        coord = Coord._make(coord)
        self.min_x = min(self.min_x, coord.x)
        self.max_x = max(self.max_x, coord.x)
        self.min_y = min(self.min_y, coord.y)
        self.max_y = max(self.max_y, coord.y)
        self.board[coord] = item

    def __getitem__(self, coord):
        return self.board[coord]

    def get(self, x, y):
        return self.board.get((x, y), ".")

    def __iter__(self):
        for y in range(self.min_y, self.max_y + 1):
            yield [self.get(x, y) for x in range(self.min_x, self.max_x + 1)]

    def add_line(self, c1, c2):
        x1, y1 = map(int, c1.split(","))
        x2, y2 = map(int, c2.split(","))
        if x1 == x2:
            y1, y2 = ordered(y1, y2)
            for y in range(y1, y2 + 1):
                self[x1, y] = "#"
        else:
            assert y1 == y2, f"{y1} != {y2}"
            x1, x2 = ordered(x1, x2)
            for x in range(x1, x2 + 1):
                self[x, y1] = "#"

    def add_sand(self):
        if self.get(500, 0) != "+":
            return False
        x = 500
        for y in range(self.max_y):
            if self.get(x, y + 1) == ".":
                continue
            if self.get(x - 1, y + 1) == ".":
                x -= 1
                continue
            if self.get(x + 1, y + 1) == ".":
                x += 1
                continue
            self[x, y] = "o"
            return True
        return False

    def plot(self):
        plt.axes().set_aspect("equal")
        plt.xticks([])
        plt.yticks([])
        plt.pcolormesh(self.colormap)
        plt.show()

    @property
    def colormap(self):
        m = {"#": 0, ".": 1, "+": 2, "o": 3}
        return [[m[c] for c in row] for row in reversed(list(self))]

    def __str__(self):
        return "\n".join("".join(row) for row in self)


def partn(part, board, animate=False, show_board=False, plot=False):

    if animate:
        if plot:
            fig = plt.figure()
            plt.xticks([])
            plt.yticks([])
            camera = Camera(fig)
        else:
            ansi_clear()
            print(f"{board}\n")
    if show_board:
        print(f"{board}\n")

    count = 0
    while board.add_sand():
        count += 1
        if animate:
            if plot:
                if part == 1 or count % 10 == 0:
                    print(f"\r{count}...", end="")
                    plt.pcolormesh(board.colormap)
                    camera.snap()
            else:
                ansi_home()
                print(f"{board}\n")
                time.sleep(1 / 60)

    if animate:
        if plot:
            print(f"\rsaving animation to part{part}.mp4 ...")
            animation = camera.animate(interval=16, blit=True)
            animation.save(f"part{part}.mp4")
        else:
            ansi_clear()
            print(f"{board}\n")

    if show_board:
        print(f"{board}\n")

    if plot and not animate:
        board.plot()

    return count


def part1(lines, animate=False, show_board=False, plot=False):
    board = Board.from_input(lines)
    return partn(1, board, animate, show_board, plot)


def part2(lines, animate=False, show_board=False, plot=False):
    board = Board.from_input(lines)
    y = board.max_y
    board.add_line(f"{board.min_x-y},{y+2}", f"{board.max_x+y},{y+2}")
    return partn(2, board, animate, show_board, plot)


def test_part1_sample():
    assert part1(SAMPLE) == 24


def test_part1_input():
    assert part1(INPUT) == 757


def test_part2_sample():
    assert part2(SAMPLE) == 93


def test_part2_input():
    assert part2(INPUT) == 24943


app = typer.Typer()


@app.command("test")
def run_pytest():
    subprocess.run(["pytest", "-v", __file__])


@app.command("part")
def run_part(
    part: int,
    sample: bool = False,
    animate: bool = False,
    show_board: bool = False,
    plot: bool = False,
):
    result = {1: part1, 2: part2}[part](
        SAMPLE if sample else INPUT,
        animate=animate,
        show_board=show_board,
        plot=plot,
    )
    print(result)


if __name__ == "__main__":
    app()
