priorities = {}    

for index, value in enumerate(range(97, 123), 1):
    priorities[chr(value)] = index

for index, value in enumerate(range(65, 91), 27):
    priorities[chr(value)] = index

with open("day3/input_day3.txt") as file_:
    input = file_.read()

    # Part 1    
    first_part = [item[:int(len(item)/2)] for item in input.split("\n")]
    second_part = [item[int(len(item)/2):] for item in input.split("\n")]

    letters_first_part = [[letter for letter in set(first)] for first in first_part]
    letters_second_part = [[letter for letter in set(first)] for first in second_part]

    total_sum_priorities_items = 0
    for index, letters in enumerate(letters_first_part):
        for letter in letters:
            if letter in letters_second_part[index]:
                total_sum_priorities_items += priorities[letter]
    print(f"{total_sum_priorities_items=}")

    # Part 2
    input_list = [item for item in input.split("\n")]

    x = 0
    y = 3
    total_sum_group_of_three_intersection = 0
    for num in range(int(len(input_list)/3)):
        group_of_three = input_list[x:y]
        intersection_letter = list(set(group_of_three[0]).intersection(group_of_three[1], group_of_three[2]))
        x+=3
        y+=3
        total_sum_group_of_three_intersection += priorities[intersection_letter[0]]
    print(f"{total_sum_group_of_three_intersection=}")
