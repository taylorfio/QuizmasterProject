import time
import os

fish_list = []
cheese_list = []
lightbulbs_list = []
score_num = 0
score = 0

restart = 1
while restart == 1:
    print("")
    print(",--.   ,--.       ,--.                                    ,--.      ")
    time.sleep(0.1)
    print("|  |   |  | ,---. |  | ,---. ,---. ,--,--,--. ,---.     ,-'  '-. ,---.   ")
    time.sleep(0.1)
    print("|  |.'.|  || .-. :|  || .--'| .-. ||        || .-. :    '-.  .-'| .-. | ")
    time.sleep(0.1)
    print("|   ,'.   |\   --.|  |\ `--.' '-' '|  |  |  |\   --.      |  |  ' '-' '    .--..--..--. ")
    time.sleep(0.1)
    print("'--'   '--' `----'`--' `---' `---' `--`--`--' `----'      `--'   `---'     '--''--''--'                                                    ,---.,---.,---. ")
    time.sleep(0.1)
    print(" ,----.                                      ,--.  ,--.               ,--.                                    ,--.  ,--.                   |   ||   ||   | ")
    time.sleep(0.1)
    print("'  .-./   ,--.,--. ,---.  ,---.  ,---.     ,-'  '-.|  ,---.  ,--,--.,-'  '-.     ,---. ,--.,--. ,---.  ,---.,-'  '-.`--' ,---. ,--,--,     |  .'|  .'|  .' ")
    time.sleep(0.1)
    print("|  | .---.|  ||  || .-. :(  .-' (  .-'     '-.  .-'|  .-.  |' ,-.  |'-.  .-'    | .-. ||  ||  || .-. :(  .-''-.  .-',--.| .-. ||      \    |  | |  | |  |  ")
    time.sleep(0.1)
    print("'  '--'  |'  ''  '\   --..-'  `).-'  `)      |  |  |  | |  |\ '-'  |  |  |      ' '-' |'  ''  '\   --..-'  `) |  |  |  |' '-' '|  ||  |    `--' `--' `--'  ")
    time.sleep(0.1)
    print(" `------'  `----'  `----'`----' `----'       `--'  `--' `--' `--`--'  `--'       `-|  | `----'  `----'`----'  `--'  `--' `---' `--''--'    .--. .--. .--.  ")
    time.sleep(0.1)
    print("                                                                                   `--'                                                    '--' '--' '--'  ")
    time.sleep(0.1)
    print("")
    print("")
    name = input("What is the name of our contestant!   ")
    print("hello ", name)
    print("")
    print("To play the game select a category then a level from 1 - 3")
    print("The higher the level the harder it is but increases the amount of points you gain ")
    print("level 1 = 100, level 2 = 200, level 3 = 300")
    print("")
# category, level

    def level_check(level_holder, category_holder):
        if category_holder == 1:
            if level_holder in fish_list:
                print("you already chose this")
                level_choice()
        if category_holder == 2:
            if level_holder in cheese_list:
                print("you already chose this")
                level_choice()
        if category_holder == 3:
            if level_holder in lightbulbs_list:
                print("you already chose this")
                level_choice()
        #else:
            #break

    def level_choice():
        level_input = input("select a level 1, 2, 3")
        if level_input.isdigit():
            level_input = int(level_input)
        while level_input != 1 and level_input != 2 and level_input != 3:
            print("error use the numbers")
            level_input = input("select a level 1, 2, 3")
            if level_input.isdigit():
                level_input = int(level_input)


        if level_input == 1:
            level_check(level_input, categories_input)
            if level_check == True:
                return 1
            elif level_check == False:
                print("you already chose this")




        if level_input == 2:
            level_check(level_input, 2)
            return 2
        if level_input == 3:
            level_check(level_input, 3)
            return 3

    def question_choice():
        global score
        print(name, "what category do you choose")
        print("Categories include:")
        print("                    1_ prehistoric fish")
        print("                    2_ cheese")
        print("                    3_ types of light bulbs")
        print("")
        categories_input = input("1, 2, 3  ")
        if categories_input.isdigit():
            categories_input = int(categories_input)
        while categories_input != 1 and categories_input != 2 and categories_input != 3:
            print("error use the numbers")
            categories_input = input("1, 2, 3  ")
            if categories_input.isdigit():
                categories_input = int(categories_input)

        if categories_input == 1:
            print("                     __    _      __             _         _____      __")
            time.sleep(0.1)
            print("    ____  ________  / /_  (_)____/ /_____  _____(_)____   / __(_)____/ /_")
            time.sleep(0.1)
            print("   / __ \/ ___/ _ \/ __ \/ / ___/ __/ __ \/ ___/ / ___/  / /_/ / ___/ __ \ ")
            time.sleep(0.1)
            print("  / /_/ / /  /  __/ / / / (__  ) /_/ /_/ / /  / / /__   / __/ (__  ) / / /")
            time.sleep(0.1)
            print(" / .___/_/   \___/_/ /_/_/____/\__/\____/_/  /_/\___/  /_/ /_/____/_/ /_/ ")
            time.sleep(0.1)
            print("/_/                                                                       ")
            time.sleep(0.1)
            print("")
            print("you chose category one - prehistoric fish")

        if categories_input == 2:
            print("        __")
            time.sleep(0.1)
            print("  _____/ /_  ___  ___  ________")
            time.sleep(0.1)
            print(" / ___/ __ \/ _ \/ _ \/ ___/ _ \ ")
            time.sleep(0.1)
            print("/ /__/ / / /  __/  __(__  )  __/")
            time.sleep(0.1)
            print("\___/_/ /_/\___/\___/____/\___/")
            time.sleep(0.1)
            print("")
            print("you chose category two - cheese")

        if categories_input == 3:
            print("   __                                 ____   ___       __    __     __          ____")
            time.sleep(0.1)
            print("  / /___  ______  ___  _____   ____  / __/  / (_)___ _/ /_  / /_   / /_  __  __/ / /_  _____")
            time.sleep(0.1)
            print(" / __/ / / / __ \/ _ \/ ___/  / __ \/ /_   / / / __ `/ __ \/ __/  / __ \/ / / / / __ \/ ___/")
            time.sleep(0.1)
            print("/ /_/ /_/ / /_/ /  __(__  )  / /_/ / __/  / / / /_/ / / / / /_   / /_/ / /_/ / / /_/ (__  )")
            time.sleep(0.1)
            print("\__/\__, / .___/\___/____/   \____/_/    /_/_/\__, /_/ /_/\__/  /_.___/\__,_/_/_.___/____/")
            time.sleep(0.1)
            print("   /____/_/                                  /____/")
            time.sleep(0.1)
            print("")
            print("you chose category three - types of light bulbs")

        a = level_choice()
        if a == 1:
            if categories_input == 1:
                if 1 in fish_list:
                    while 1 in fish_list:
                        level_choice()
                elif 1 not in fish_list:
                    answer = 1
                    fish_list.append(1)
                    score_num = 100
                    try:
                        question1 = open("question 1.txt", "r")
                        temp = question1.readlines()
                        print(temp[4])
                        print(temp[5])
                        print(temp[6])
                        print(temp[7])
                        print(temp[8])
                    except:
                        print("ERROR")
            elif categories_input == 2:
                if 1 in cheese_list:
                    while 1 in cheese_list:
                        level_choice()

                elif 1 not in cheese_list:
                    answer = 1
                    cheese_list.append(1)
                    score_num = 100
                    try:
                        question1 = open("question 1.txt", "r")
                        temp = question1.readlines()
                        print(temp[30])
                        print(temp[31])
                        print(temp[32])
                        print(temp[33])
                        print(temp[34])
                    except:
                        print("ERROR")
            elif categories_input == 3:
                if 1 in lightbulbs_list:
                    while 1 in lightbulbs_list:
                        level_choice()

                elif 1 not in lightbulbs_list:
                    answer = 1
                    lightbulbs_list.append(1)
                    score_num = 100
                    try:
                        question1 = open("question 1.txt", "r")
                        temp = question1.readlines()
                        print(temp[56])
                        print(temp[57])
                        print(temp[58])
                        print(temp[59])
                        print(temp[60])
                    except:
                        print("ERROR")

        if a == 2:
            if categories_input == 1:
                if 2 in fish_list:
                    while 1 in fish_list:
                        level_choice()
                if 2 not in fish_list:
                    answer = 2
                    fish_list.append(2)
                    score_num = 200
                    try:
                        question1 = open("question 1.txt", "r")
                        temp = question1.readlines()
                        print(temp[12])
                        print(temp[13])
                        print(temp[14])
                        print(temp[15])
                        print(temp[16])
                    except:
                        print("ERROR")
            if categories_input == 2:
                if 2 in cheese_list:
                    while 1 in cheese_list:
                        level_choice()
                if 2 not in cheese_list:
                    answer = 2
                    cheese_list.append(2)
                    score_num = 200
                    try:
                        question1 = open("question 1.txt", "r")
                        temp = question1.readlines()
                        print(temp[38])
                        print(temp[39])
                        print(temp[40])
                        print(temp[41])
                        print(temp[42])
                    except:
                        print("ERROR")
            if categories_input == 3:
                if 2 in lightbulbs_list:
                    while 1 in lightbulbs_list:
                        level_choice()
                if 2 not in lightbulbs_list:
                    answer = 2
                    lightbulbs_list.append(2)
                    score_num = 200
                    try:
                        question1 = open("question 1.txt", "r")
                        temp = question1.readlines()
                        print(temp[64])
                        print(temp[65])
                        print(temp[66])
                        print(temp[67])
                        print(temp[68])
                    except:
                        print("ERROR")
        if a == 3:
            if categories_input == 1:
                if 3 in fish_list:
                    while 3 in fish_list:
                        level_choice()
                if 3 not in fish_list:
                    answer = 3
                    fish_list.append(3)
                    score_num = 300
                    try:
                        question1 = open("question 1.txt", "r")
                        temp = question1.readlines()
                        print(temp[20])
                        print(temp[21])
                        print(temp[22])
                        print(temp[23])
                        print(temp[24])
                    except:
                        print("ERROR")
            if categories_input == 2:
                if 3 in cheese_list:
                    while 3 in cheese_list:
                        level_choice()
                if 3 not in cheese_list:
                    answer = 3
                    cheese_list.append(3)
                    score_num = 300
                    try:
                        question1 = open("question 1.txt", "r")
                        temp = question1.readlines()
                        print(temp[46])
                        print(temp[47])
                        print(temp[48])
                        print(temp[49])
                        print(temp[50])
                    except:
                        print("ERROR")
            if categories_input == 3:
                if 3 in lightbulbs_list:
                    while 3 in lightbulbs_list:
                        level_choice()
                if 3 not in lightbulbs_list:
                    answer = 3
                    lightbulbs_list.append(3)
                    score_num = 300
                    try:
                        question1 = open("question 1.txt", "r")
                        temp = question1.readlines()
                        print(temp[72])
                        print(temp[73])
                        print(temp[74])
                        print(temp[75])
                        print(temp[76])
                    except:
                        print("ERROR")

        question_answer = int(input("1, 2, 3 or 4"))
        while question_answer != 1 and question_answer != 2 and question_answer != 3 and question_answer != 4:  # defencive coding
            print("error")
            question_answer = input("1, 2, 3 or 4")
        if question_answer == answer:
            score = score + score_num
            print("correct! your score is now ", score)
        elif question_answer != answer:
            print("incorrect! your score is ", score)

    while len(fish_list) != 3 and len(cheese_list) != 3 and len(lightbulbs_list) != 3:
        question_choice()
    else:
        print("you have answered all the questions")

        # save score here


        ending = input("do you want to restart: yes or no  ")  # code to restart the entire game
        while ending != "no" and ending != "yes":  # defencive coding
            print("error")
            ending = input("do you want to restart: yes or no  ")
        if ending == "no":
            restart = restart + 1
        elif ending == "yes":
            restart = restart + 0



