with open("day4/input_day4.txt") as file_:
    input = file_.read()
    pairs = input.split("\n")

    # Part 1
    total_constains = 0
    for pair in pairs:
        elf1, elf2 = pair.split(",")

        start1, end1 = elf1.split("-")
        start2, end2 = elf2.split("-")

        start1 = int(start1)
        end1 = int(end1)+1
        start2 = int(start2)
        end2 = int(end2)+1

        is_all_contained = True
        for i in range(start1, end1):
            if i in range(start2, end2):
                continue
            else:
                is_all_contained = False
                break

        if not is_all_contained:
            is_all_contained = True
            for i in range(start2, end2):
                if i in range(start1, end1):
                    continue
                else:
                    is_all_contained = False
                    break

        if is_all_contained:
            total_constains+=1
    print(total_constains)

    # Part 2
    total_constains = 0
    for pair in pairs:
        elf1, elf2 = pair.split(",")

        start1, end1 = elf1.split("-")
        start2, end2 = elf2.split("-")

        start1 = int(start1)
        end1 = int(end1)+1
        start2 = int(start2)
        end2 = int(end2)+1

        is_contained = False
        for i in range(start1, end1):
            if i in range(start2, end2):
                is_contained = True
                break
            else:
                continue

        if not is_contained:
            for i in range(start2, end2):
                if i in range(start1, end1):
                    is_contained = True
                    break
                else:
                    continue

        if is_contained:
            total_constains+=1

    print(total_constains)
