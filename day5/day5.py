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

# Part 1
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


def move_crates(qty: int, stack_from: str, stack_to: str):
    for _ in range(qty):
        stacks[stack_to].append(stacks[stack_from].pop())

def move_crates_reverse(qty: int, stack_from: str, stack_to: str):
    crates_pop = []
    for _ in range(qty):
        try:
            crates_pop.append(stacks[stack_from].pop())
        except:
            print("")
    crates_pop.reverse()
    stacks[stack_to].extend(crates_pop)

def get_qty(move: str):
    qty = move.replace("move ", "").strip()
    return int(qty)

def get_stacks_position(move: str):
    stack_from, stack_to = move.split("to")
    return stack_from.strip(), stack_to.strip()


with open("day5/input_day5.txt") as file_:
    input = file_.read()

    for move in input.split("\n"):
        move_splitted = move.split("from")
        qty = get_qty(move_splitted[0])
        stack_from, stack_to = get_stacks_position(move_splitted[1])

        move_crates(qty, stack_from, stack_to)

    final_crates_on_top = []
    for values in stacks.values():
        final_crates_on_top.append(values.pop())

    print("".join(final_crates_on_top))


# Part 2
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

with open("day5/input_day5.txt") as file_:
    input = file_.read()

    for move in input.split("\n"):
        move_splitted = move.split("from")
        qty = get_qty(move_splitted[0])
        stack_from, stack_to = get_stacks_position(move_splitted[1])

        move_crates_reverse(qty, stack_from, stack_to)

    final_crates_on_top = []
    for values in stacks.values():
        final_crates_on_top.append(values.pop())

    print("".join(final_crates_on_top))