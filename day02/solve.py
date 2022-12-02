#!/opt/homebrew/bin/python3
"""
https://adventofcode.com/2022/day/1


"""
from pathlib import Path

HERE = Path(__file__).parent
INPUT = (HERE / "input.txt").read_text().strip()
# INPUT = (HERE / "sample.txt").read_text().strip()


def part1():
    ROCK, PAPER, SCISSORS = "Rock", "Paper", "Scissors"
    WIN, LOSE, DRAW = "Win", "Lose", "Draw"
    SCORES = {ROCK: 1, PAPER: 2, SCISSORS: 3, LOSE:0, DRAW:3, WIN:6}
    C1 = {"A": ROCK, "B": PAPER, "C": SCISSORS}
    C2 = {"X": ROCK, "Y": PAPER, "Z": SCISSORS}
    total = 0
    for line in INPUT.splitlines():
        c1, c2 = line.split()
        s1 = C1[c1]
        s2 = C2[c2]
        if s1 == s2:
            outcome = DRAW
        elif (s1, s2) == (ROCK, SCISSORS):
            outcome = LOSE
        elif (s1, s2) == (ROCK, PAPER):
            outcome = WIN
        elif (s1, s2) == (PAPER, ROCK):
            outcome = LOSE
        elif (s1, s2) == (PAPER, SCISSORS):
            outcome = WIN
        elif (s1, s2) == (SCISSORS, ROCK):
            outcome = WIN
        elif (s1, s2) == (SCISSORS, PAPER):
            outcome = LOSE
        score = SCORES[s2] + SCORES[outcome]
        total += score
        # print(score)
    print(total)


def part2():
    ROCK, PAPER, SCISSORS = "Rock", "Paper", "Scissors"
    WIN, LOSE, DRAW = "Win", "Lose", "Draw"
    SCORES = {ROCK: 1, PAPER: 2, SCISSORS: 3, LOSE:0, DRAW:3, WIN:6}
    C1 = {"A": ROCK, "B": PAPER, "C": SCISSORS}
    C2 = {"X": LOSE, "Y": DRAW, "Z": WIN}
    total = 0
    for line in INPUT.splitlines():
        c1, c2 = line.split()
        s1 = C1[c1]
        outcome = C2[c2]
        if outcome == WIN:
            s2 = {
                ROCK: PAPER,
                PAPER: SCISSORS,
                SCISSORS: ROCK,
            }[s1]
        elif outcome == LOSE:
            s2 = {
                ROCK: SCISSORS,
                PAPER: ROCK,
                SCISSORS: PAPER,
            }[s1]
        else:
            assert outcome == DRAW
            s2 = s1
        score = SCORES[s2] + SCORES[outcome]
        total += score
        # print(f"{outcome} to {s1} = {s2} ({score})")
    print(total)


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
