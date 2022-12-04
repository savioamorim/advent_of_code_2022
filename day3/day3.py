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

    share_items = []
    total_sum = 0
    for index, letters in enumerate(letters_first_part):
        for letter in letters:
            if letter in letters_second_part[index]:
                share_items.append(letter)
                total_sum += priorities[letter]

    print(total_sum)

    # Part 2
    input_list = [item for item in input.split("\n")]

    x = 0
    y = 3
    share_items = []
    for num in range(int(len(input_list)/3)):
        group_of_three = input_list[x:y]
        share_items.append(list(set(list(group_of_three[0])).intersection(list(set(group_of_three[1])), list(set(group_of_three[2])))))
        x+=3
        y+=3
    
    total_sum = 0
    for item in share_items:
        total_sum += priorities[item[0]]
    print(total_sum)
