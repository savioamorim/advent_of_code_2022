"""
[F]         [L]     [M]            
[T]     [H] [V] [G] [V]            
[N]     [T] [D] [R] [N]     [D]    
[Z]     [B] [C] [P] [B] [R] [Z]    
[M]     [J] [N] [M] [F] [M] [V] [H]
[G] [J] [L] [J] [S] [C] [G] [M] [F]
[H] [W] [V] [P] [W] [H] [H] [N] [N]
[J] [V] [G] [B] [F] [G] [D] [H] [G]
 1   2   3   4   5   6   7   8   9 
"""

from copy import deepcopy
from typing import Dict, List


stacks = {
    "1": ["J", "H", "G", "M", "Z", "N", "T", "F"],
    "2": ["V", "W", "J"],
    "3": ["G", "V", "L", "J", "B", "T", "H"],
    "4": ["B", "P", "J", "N", "C", "D", "V", "L"],
    "5": ["F", "W", "S", "M", "P", "R", "G"],
    "6": ["G", "H", "C", "F", "B", "N", "V", "M"],
    "7": ["D", "H", "G", "M", "R"],
    "8": ["H", "N", "M", "V", "Z", "D"],
    "9": ["G", "N", "F", "H"],
}


def move_crates(qty: int, stack_from: str, stack_to: str) -> None:
    for _ in range(qty):
        stacks_part_1[stack_to].append(stacks_part_1[stack_from].pop())

def move_crates_reverse(qty: int, stack_from: str, stack_to: str) -> None:
    crates_pop = []
    for _ in range(qty):
        crates_pop.append(stacks_part_2[stack_from].pop())
    crates_pop.reverse()
    stacks_part_2[stack_to].extend(crates_pop)

def get_qty(move: str) -> int:
    qty = move.replace("move ", "").strip()
    return int(qty)

def get_stacks_position(move: str) -> str:
    stack_from, stack_to = move.split("to")
    return stack_from.strip(), stack_to.strip()

def get_top_crates(stack: Dict[str, List[str]]) -> str:
    final_crates_on_top = []
    for values in stack.values():
        final_crates_on_top.append(values.pop())
    return "".join(final_crates_on_top)

with open("day5/input_day5.txt") as file_:
    input = file_.read()

    stacks_part_1 = deepcopy(stacks)
    stacks_part_2 = deepcopy(stacks)

    for move in input.split("\n"):
        move_splitted = move.split("from")
        qty = get_qty(move_splitted[0])
        stack_from, stack_to = get_stacks_position(move_splitted[1])

        # Part 1
        move_crates(qty, stack_from, stack_to)
        # Part 2
        move_crates_reverse(qty, stack_from, stack_to)

    print("Part 1 top crates:", get_top_crates(stacks_part_1))
    print("Part 2 top crates:", get_top_crates(stacks_part_2))
