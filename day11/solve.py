#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/11
"""
from pathlib import Path
from functools import partial, reduce
from operator import add, mul
import re

HERE = Path(__file__).parent
SAMPLE = (HERE / "sample.txt").read_text().strip().splitlines()
INPUT = (HERE / "input.txt").read_text().strip().splitlines()


class Monkey:
    def __init__(self, n, lines):
        self.n = n
        self.count = 0
        # Starting items: 79, 98
        m = re.search(r"Starting items: (.*)", next(lines))
        self.items = [int(i) for i in m.group(1).split(",")]

        # Operation: new = old * 19
        m = re.search(r"Operation: new = old (.) (old|\d+)", next(lines))
        op = {"+": add, "*": mul}[m.group(1)]
        if m.group(2) == "old":
            self.op = lambda x: op(x, x)
        else:
            self.op = partial(op, int(m.group(2)))

        # Test: divisible by 23
        m = re.search(r"Test: divisible by (\d+)", next(lines))
        self.factor = int(m.group(1))

        # If true: throw to monkey 2
        m = re.search(r"If true: throw to monkey (\d+)", next(lines))
        self.true = int(m.group(1))

        # If false: throw to monkey 3
        m = re.search(r"If false: throw to monkey (\d+)", next(lines))
        self.false = int(m.group(1))

    def catch(self, item):
        self.items.append(item)

    def play_turn(self, monkeys, scale_item, debug=False):
        log = self.log if debug else lambda *args: None
        for item in self.items:
            self.count += 1
            item = scale_item(self.op(item))
            n = self.true if item % self.factor == 0 else self.false
            log(f"throwing {item} to {n}")
            monkeys[n].catch(item)
        self.items[:] = []

    def log(self, msg):
        print(f"Monkey {self.n}: {msg}")

    def __str__(self):
        items = ", ".join(str(i) for i in self.items)
        return f"Monkey {self.n}: {items}"


def make_monkeys(lines):
    monkeys = []
    lines = iter(lines)
    while lines:
        m = re.search(r"^Monkey (\d+):", next(lines))
        monkeys.append(Monkey(m.group(1), lines))
        try:
            next(lines)
        except StopIteration:
            break
    return monkeys


def part1(lines, debug=False):
    log = print if debug else lambda *args: None
    monkeys = make_monkeys(lines)
    scale_item = lambda item: item // 3
    for i in range(20):
        log(f"Round {i+1}:")
        for monkey in monkeys:
            monkey.play_turn(monkeys, scale_item)
        for monkey in monkeys:
            log(monkey)
        log()
    if debug:
        for monkey in monkeys:
            monkey.log(f"inspected items {monkey.count} times.")
    return mul(*list(reversed(sorted(m.count for m in monkeys)))[:2])


def part2(lines, debug=False):
    monkeys = make_monkeys(lines)
    # I needed a hint for this. This was not math I remembered.
    # Multiply the divisors by each other then take the modulo
    # of each item each time it's played.
    modulo = reduce(mul, [m.factor for m in monkeys])
    scale_item = lambda item: item % modulo
    for i in range(1, 10001):
        for monkey in monkeys:
            monkey.play_turn(monkeys, scale_item)
        if debug and (i % 1000 == 0 or i in (1, 20)):
            print(f"After round {i}:")
            for monkey in monkeys:
                monkey.log(f"inspected items {monkey.count} times.")
    return mul(*list(reversed(sorted(m.count for m in monkeys)))[:2])


def test():
    assert part1(SAMPLE) == 10605
    assert part2(SAMPLE) == 2713310158
    assert part1(INPUT) == 90294
    assert part2(INPUT) == 18170818354


def main():
    test()
    print(part1(INPUT))
    print(part2(INPUT))


if __name__ == "__main__":
    main()
