#!/opt/homebrew/bin/python3
"""
https://adventofcode.com/2022/day/2
"""
from pathlib import Path

HERE = Path(__file__).parent
INPUT = (HERE / "input.txt").read_text().strip()
# INPUT = (HERE / "sample.txt").read_text().strip()

ROCK, PAPER, SCISSORS = "Rock", "Paper", "Scissors"
WIN, LOSE, DRAW = "Win", "Lose", "Draw"
SCORES = {ROCK: 1, PAPER: 2, SCISSORS: 3, LOSE: 0, DRAW: 3, WIN: 6}
C1 = {"A": ROCK, "B": PAPER, "C": SCISSORS}


def part1():
    C2 = {"X": ROCK, "Y": PAPER, "Z": SCISSORS}
    OUTCOMES = {
        # s1, s2: s2 outcome
        (ROCK, ROCK): DRAW,
        (ROCK, PAPER): WIN,
        (ROCK, SCISSORS): LOSE,
        (PAPER, ROCK): LOSE,
        (PAPER, PAPER): DRAW,
        (PAPER, SCISSORS): WIN,
        (SCISSORS, ROCK): WIN,
        (SCISSORS, PAPER): LOSE,
        (SCISSORS, SCISSORS): DRAW,
    }
    total = 0
    for line in INPUT.splitlines():
        c1, c2 = line.split()
        s1, s2 = C1[c1], C2[c2]
        outcome = OUTCOMES[(s1, s2)]
        score = SCORES[s2] + SCORES[outcome]
        total += score
        # print(score)
    print(total)


def part2():
    C2 = {"X": LOSE, "Y": DRAW, "Z": WIN}
    SHAPES = {
        # s1, s2 outcome: s2
        (ROCK, DRAW): ROCK,
        (ROCK, WIN): PAPER,
        (ROCK, LOSE): SCISSORS,
        (PAPER, LOSE): ROCK,
        (PAPER, DRAW): PAPER,
        (PAPER, WIN): SCISSORS,
        (SCISSORS, WIN): ROCK,
        (SCISSORS, LOSE): PAPER,
        (SCISSORS, DRAW): SCISSORS,
    }
    total = 0
    for line in INPUT.splitlines():
        c1, c2 = line.split()
        s1, outcome = C1[c1], C2[c2]
        s2 = SHAPES[(s1, outcome)]
        score = SCORES[s2] + SCORES[outcome]
        total += score
        # print(f"{outcome} to {s1} = {s2} ({score})")
    print(total)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
