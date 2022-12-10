#!/usr/bin/env python3.11
"""
https://adventofcode.com/2022/day/8
"""
import time
from collections import namedtuple
from pathlib import Path

HERE = Path(__file__).parent
INPUT = (HERE / "input.txt").read_text()
SAMPLE = (HERE / "sample.txt").read_text()
SAMPLE2 = (HERE / "sample2.txt").read_text()

Knot = namedtuple("Knot", "c x y")


def draw_board(knots, final=False, size=None):
    min_x = min(knot.x for knot in knots)
    max_x = max(knot.x for knot in knots)
    min_y = min(knot.y for knot in knots)
    max_y = max(knot.y for knot in knots)
    off_x = abs(min_x) if min_x < 0 else 0
    off_y = abs(min_y) if min_y < 0 else 0
    min_x += off_x
    max_x += off_x
    min_y += off_y
    max_y += off_y

    size_x, size_y = size if size else (0, 0)
    size_x = max(max(max_x + 1, off_x + 1, 6), size_x)
    size_y = max(max(max_y + 1, off_y + 1, 5), size_y)
    rows = [["."] * size_x for _ in range(size_y)]

    for knot in reversed(knots):
        rows[knot.y + off_y][knot.x + off_x] = "#" if final else knot.c

    rows[off_y][off_x] = "X"

    rows = [
        f"{''.join(row)} {size_y-off_y-i:4}"
        for i, row in enumerate(reversed(rows), 1)
    ]
    if size:
        rows = rows[-size[1] :] if off_y else rows[: size[1]]

    legend = [str(off_x - i)[-1] for i in range(size_x)]
    legend[off_x] = "|"
    rows.append("")
    rows.append("".join(legend))

    return "\n".join(rows) + "\n"


def limit(a, i, b):
    return min(max(a, i), b)


class Rope:
    def __init__(self, length=2, debug=False):
        chars = (
            "HT"
            if length == 2
            else "H" + "".join(str(i) for i in range(1, length + 1))
        )
        self.knots = [Knot(c, 0, 0) for c in chars]
        self.tails = {self.knots[-1]}
        self._debug = debug
        self.animate = False
        self.moves = 0

    def debug(self, arg0, *args, **kwargs):
        if self._debug:
            if callable(arg0):
                arg0 = arg0(*args, **kwargs)
            print(arg0)

    def move(self, move):
        direction, amount = move.split()
        self.debug(f"== {direction} {amount} ==")
        self.moves += 1
        for _ in range(int(amount)):
            self._move_one(direction)
            self.tails.add(self.knots[-1])
            self.debug(draw_board, self.knots)
            if self.animate:
                print("\033[2J\033[1;1H", end="")
                print(draw_board(self.knots, final=True, size=self.animate))
                print(self.moves)
                time.sleep(1 / 60)

    def __len__(self):
        self.debug(draw_board, self.tails, True)
        return len(self.tails)

    def _move_one(self, direction):
        x, y = {
            "U": (0, 1),
            "D": (0, -1),
            "L": (-1, 0),
            "R": (1, 0),
        }[direction]
        head = self.knots[0]
        self.knots[0] = head._replace(x=head.x + x, y=head.y + y)
        for i in range(1, len(self.knots)):
            head, knot = self.knots[i - 1], self.knots[i]
            dx, dy = head.x - knot.x, head.y - knot.y
            if abs(dx) < 2 and abs(dy) < 2:
                x, y = 0, 0
            else:
                x, y = limit(-1, dx, 1), limit(-1, dy, 1)
            self.knots[i] = knot._replace(x=knot.x + x, y=knot.y + y)


def part1(lines, debug=False):
    rope = Rope(debug=debug)
    for line in lines:
        rope.move(line)
    return len(rope)


def part2(lines, debug=False):
    rope = Rope(length=9, debug=debug)
    for line in lines:
        rope.move(line)
    return len(rope)


def test():
    sample = SAMPLE.splitlines()
    assert part1(sample) == 13, part1(sample, True)
    assert part2(sample) == 1, part2(sample, True)
    sample2 = SAMPLE2.splitlines()
    assert part2(sample2) == 36, part2(sample2, True)


def animate(lines):
    rope = Rope(length=9)
    rope.animate = (80, 25)
    for line in lines:
        rope.move(line)


def main():
    test()
    lines = INPUT.splitlines()
    result = part1(lines)
    assert result == 6190, result
    print(result)

    result = part2(lines)
    assert result == 2516, result
    print(result)

    animate(lines)


if __name__ == "__main__":
    main()
