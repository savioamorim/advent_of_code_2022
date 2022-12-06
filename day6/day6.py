RANGE_PART_1 = 4
RANGE_PART_2 = 14

def find_duplicates(range: int, characters: str):
    sliced_characters = []
    sliced_characters = characters[character:character+range]
    return True if [x for x in sliced_characters if sliced_characters.count(x) > 1] else False

with open("day6/input_day6.txt") as file_:
    input = file_.read()

    found = False
    for character in range(len(input)):
        # Part 1
        if not found and not find_duplicates(RANGE_PART_1, input):
            print(f"Position group of 4: {character+RANGE_PART_1}")
            found = True

        # Part 2
        if not find_duplicates(RANGE_PART_2, input):
            print(f"Position group of 14: {character+RANGE_PART_2}")
            break
