def find_all_contained_range(start1, end1, start2, end2):
    is_all_contained = True
    for i in range(start1, end1):
        if i in range(start2, end2):
            continue
        else:
            is_all_contained = False
            break
    return is_all_contained

def find_any_contained_range(start1, end1, start2, end2):
    is_contained = False
    for i in range(start1, end1):
        if i in range(start2, end2):
            is_contained = True
            break
        else:
            continue
    return is_contained

def get_start_end_range(elf_range):
    start, end = elf_range.split("-")
    return int(start), int(end)+1


with open("day4/input_day4.txt") as file_:
    input = file_.read()
    pairs = input.split("\n")

    total_all_constains = 0
    total_any_constains = 0
    for pair in pairs:
        elf1, elf2 = pair.split(",")

        start1, end1 = get_start_end_range(elf1)
        start2, end2 = get_start_end_range(elf2)

        # Part 1
        is_all_contained = find_all_contained_range(start1, end1, start2, end2)
        if not is_all_contained:
            is_all_contained = find_all_contained_range(start2, end2, start1, end1)

        if is_all_contained:
            total_all_constains+=1

        # Part 2
        is_any_contained = find_any_contained_range(start1, end1, start2, end2)
        if not is_any_contained:
            find_any_contained_range(start2, end2, start1, end1)

        if is_any_contained:
            total_any_constains += 1

    print(f"{total_all_constains=}")
    print(f"{total_any_constains=}")
