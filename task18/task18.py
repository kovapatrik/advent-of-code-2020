import re
from collections import deque
from math import prod
from operator import add, mul


def equal_precedence(tokens, operators={'+': add, '*': mul}):
    tokens = deque(tokens.split())
    res = int(tokens.popleft())
    while tokens:
        op, nr = tokens.popleft(), int(tokens.popleft())
        res = operators[op](res, nr)
    return res


def add_before(tokens):
    # can use eval instead of equal_precedence, but it's 5x slower
    return prod(map(equal_precedence, tokens.split("*")))


def evaluate(tokens, inner_eval, brackets_regex=re.compile(r'(\([^()]+\))')):
    inside_brackets = brackets_regex.search(tokens)
    if not inside_brackets:
        return inner_eval(tokens)
    inside_brackets = inside_brackets.group(1)
    brackets_result = inner_eval(inside_brackets.strip('()'))
    new_tokens = tokens.replace(inside_brackets, str(brackets_result))
    return evaluate(new_tokens, inner_eval)


def solve_first(lines):
    return sum(evaluate(line, equal_precedence) for line in lines)


def solve_second(lines):
    return sum(evaluate(line, add_before) for line in lines)


def parse_input(input_str):
    return input_str.splitlines()


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        print(solve_first(lines))
        print(solve_second(lines))