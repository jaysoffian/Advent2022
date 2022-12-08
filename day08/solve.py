#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/8
"""
from pathlib import Path

HERE = Path(__file__).parent
INPUT = (HERE / "input.txt").read_text()
SAMPLE = (HERE / "sample.txt").read_text()


def xy_iter(i, j):
    for x in range(1, i - 1):
        for y in range(1, j - 1):
            yield x, y


def tree_iter(lines):
    table = [list(map(int, line)) for line in lines]
    num_rows = len(table)
    num_cols = len(table[0])
    for row, col in xy_iter(num_rows, num_cols):
        height = table[row][col]
        row_heights = table[row]
        col_heights = [table[i][col] for i in range(num_rows)]
        up = col_heights[:row]
        left = row_heights[:col]
        right = row_heights[col + 1 :]
        down = col_heights[row + 1 :]
        yield height, up, left, right, down


def part1(lines):
    def is_visible(height, heights):
        return height > max(heights)

    num_visible = len(lines) * 2 + len(lines[0]) * 2 - 4
    for height, up, left, right, down in tree_iter(lines):
        if (
            is_visible(height, up)
            or is_visible(height, left)
            or is_visible(height, right)
            or is_visible(height, down)
        ):
            num_visible += 1
    return num_visible


def part2(lines):
    def viewing_distance(height, heights):
        for i, other_height in enumerate(heights, 1):
            if other_height >= height:
                return i
        return i

    max_score = 0
    for height, up, left, right, down in tree_iter(lines):
        max_score = max(
            max_score,
            viewing_distance(height, reversed(up))
            * viewing_distance(height, reversed(left))
            * viewing_distance(height, right)
            * viewing_distance(height, down),
        )
    return max_score


def test():
    lines = SAMPLE.splitlines()
    assert part1(lines) == 21
    assert part2(lines) == 8


def main():
    test()
    lines = INPUT.splitlines()
    print(part1(lines))
    print(part2(lines))


if __name__ == "__main__":
    main()
