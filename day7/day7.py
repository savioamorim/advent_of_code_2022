import os

def calculate_directory_size(directory):
    size = directory_size[directory]
    for dir in directory_structure[directory]:
        if dir in directory_structure:
            size += calculate_directory_size(dir)
    return size

with open("day7/input_day7.txt") as file_:
    input = file_.read()

    directory_structure = {}
    directory_size = {}

    for command in input.split("\n"):
        if "$ ls" in command:
            continue
        elif "$ cd" in command:
            _, cmd, directory = command.split(" ")
            if directory == "/":
                current_directory = directory
            else:
                current_directory = os.path.normpath(os.path.join(current_directory, directory))
            if current_directory not in directory_structure:
                directory_structure[current_directory] = []
                directory_size[current_directory] = 0
        elif "dir " in command:
            cmd, directory = command.split(" ")
            directory_structure[current_directory].append(os.path.join(current_directory, directory))
        else:
            file_size, file_name = command.split(" ")
            directory_size[current_directory] += int(file_size)

    # Part 1
    DIR_AT_MOST_SIZE = 100000

    total_size = 0
    for directory in directory_structure:
        size = calculate_directory_size(directory)
        if size <= DIR_AT_MOST_SIZE:
            total_size += size
    print(f"{total_size=}")

    # Part 2
    TOTAL_SPACE_AVAILABLE = 70000000
    REQUIRED_SPACE = 30000000

    used_space = calculate_directory_size("/")
    unused_space = TOTAL_SPACE_AVAILABLE - used_space
    min_space_required = REQUIRED_SPACE - unused_space

    smallest_possible_directory = TOTAL_SPACE_AVAILABLE
    for directory in directory_size:
        size = calculate_directory_size(directory)
        if min_space_required <= size <= smallest_possible_directory:
            smallest_possible_directory = size
    print(f"{smallest_possible_directory=}")
