me_part1 = {
    "X": 1,  #Rock
    "Y": 2,  #Paper
    "Z": 3,  #Scissors
}

results_part1 = {
    "A X": 3,
    "A Y": 6,
    "A Z": 0,
    "B X": 0,
    "B Y": 3,
    "B Z": 6,
    "C X": 6,
    "C Y": 0,
    "C Z": 3,
}

###########################
###########################

result_part2 = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}

me_part2 = {
    "A X": 3,
    "A Y": 1,
    "A Z": 2,
    "B X": 1,
    "B Y": 2,
    "B Z": 3,
    "C X": 2,
    "C Y": 3,
    "C Z": 1,
}

with open("day2/input_day2.txt") as file_:
    input = file_.read()
    
    games = [game for game in input.split("\n")]
    
    # Part 1
    games_score = sum([results_part1[game] for game in games])
    
    my_choose = [[choose for choose in chooses.split(" ")][1] for chooses in games]
    choose_score = sum([me_part1[num] for num in my_choose])

    print(games_score + choose_score)

    # Part 2
    result_games = [[choose for choose in chooses.split(" ")][1] for chooses in games]
    choose_score = sum([result_part2[result] for result in result_games])
    
    games_score = sum([me_part2[game] for game in games])
    print(games_score + choose_score)
    
