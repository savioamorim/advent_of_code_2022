with open("day6/input_day6.txt") as file_:
    input = file_.read()
    
    characters = list(input)
    found = False
    for character in range(len(characters)):
        # Part 1
        four_characters = []
        four_characters = characters[character:character+4]
        duplicates = [x for x in four_characters if four_characters.count(x) > 1]

        if not duplicates and not found:
            print(f"{four_characters=}")
            print(f"Position: {character+4}")
            found = True

        # Part 2
        fourteen_characters = []
        fourteen_characters = characters[character:character+14]
        duplicates = [x for x in fourteen_characters if fourteen_characters.count(x) > 1]
        if not duplicates:
            print(f"{fourteen_characters=}")
            print(f"Position: {character+14}")
            break
