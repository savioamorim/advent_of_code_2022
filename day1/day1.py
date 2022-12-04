with open("day1/input_day1.txt") as file_:
    input = file_.read()
    elven_block = [item for item in input.split("\n\n")]

    #Part 1
    max_cal = max([sum([int(cal) for cal in item.split("\n")]) for item in elven_block])
    print(max_cal)
    
    #Part 2
    test = [sum([int(cal) for cal in item.split("\n")]) for item in elven_block]
    test.sort(reverse=True)
    print(sum(test[:3]))
