#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/2
"""
from pathlib import Path

HERE = Path(__file__).parent
INPUT = (HERE / "input.txt").read_text().strip()
# INPUT = (HERE / "sample.txt").read_text().strip()

SCORES = {
    "R": 1,  # Rock
    "P": 2,  # Paper
    "S": 3,  # Scissors
    "L": 0,  # Lose
    "D": 3,  # Draw
    "W": 6,  # Win
}
RULES = [
    # Player 1's shape indexes the row.
    # Player 2's shape indexes the column.
    # W, L or D is the outcome for player 2.
    # RPS
    "DWL",  # R
    "LDW",  # P
    "WLD",  # S
]


def part1():
    total = 0
    for line in INPUT.splitlines():
        c1, c2 = line.split()
        s1 = "RPS"["ABC".index(c1)]
        s2 = "RPS"["XYZ".index(c2)]
        outcome = RULES["RPS".index(s1)]["RPS".index(s2)]
        score = SCORES[s2] + SCORES[outcome]
        total += score
    assert total == 14375, total
    print(total)


def part2():
    total = 0
    for line in INPUT.splitlines():
        c1, c2 = line.split()
        s1 = "RPS"["ABC".index(c1)]
        outcome = "LDW"["XYZ".index(c2)]
        s2 = "RPS"[RULES["RPS".index(s1)].index(outcome)]
        assert RULES["RPS".index(s1)]["RPS".index(s2)] == outcome
        score = SCORES[s2] + SCORES[outcome]
        total += score
    assert total == 10274, total
    print(total)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
