import time

''' in this multiple choice game show you select a category and a level. The program takes your input then checks 
if they had been entered before by comparing them to a list. if the values come out true they go through a function
that finds the corresponding answer and score value and the question to print. when you go through all the questions
the game ends and asks you if you want to save your score were your name is added to savefile.txt. then the program 
sks if you want to restart or finish.'''

restart = 1
while restart == 1:  # puts the program in a while loop that continues until told to stop
    fish_list = []
    cheese_list = []  # stating the lists and variables at the beginning of the program
    lightbulbs_list = []
    score = 0

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
    name = input("What is the name of our contestant!   ")  # takes the users name
    print("hello ", name)
    print("")
    print("To play the game select a category then a level from 1 - 3")
    print("The higher the level the harder it is but increases the amount of points you gain ")
    print("level 1 = 100, level 2 = 200, level 3 = 300")  # explains the rules of the game
    print("")

    def level_choice():  # function that takes the users input for level and categories and checks if it has been used already
        print(name, "what category do you choose")
        print("Categories include:")
        print("                    1_ prehistoric fish")
        print("                    2_ cheese")
        print("                    3_ types of light bulbs")
        print("")
        categories_input = input("1, 2, 3  ")  # takes the category input
        if categories_input.isdigit():
            categories_input = int(categories_input)  # makes sure the input is a integer because quotes are annoying
        while categories_input != 1 and categories_input != 2 and categories_input != 3:
            print("error use the numbers")  # defencive coding
            categories_input = input("1, 2, 3  ")
            if categories_input.isdigit():
                categories_input = int(categories_input)

        level_input = input("select a level 1, 2, 3")  # takes the level input
        if level_input.isdigit():
            level_input = int(level_input)  # makes sure the input is a integer
        while level_input != 1 and level_input != 2 and level_input != 3:
            print("error use the numbers")  # defencive coding
            level_input = input("select a level 1, 2, 3")
            if level_input.isdigit():
                level_input = int(level_input)

        if categories_input == 1:
            if level_input in fish_list:  # checks if the category and level had already been selected
                b = False
            else:
                b = True
        if categories_input == 2:
            if level_input in cheese_list:
                b = False
            else:
                b = True
        if categories_input == 3:
            if level_input in lightbulbs_list:
                b = False
            else:
                b = True

        if b == True:
            return [categories_input, level_input]  # if it hasn't it returns the category and level input
        elif b == False:
            print("you already chose this")  # if it has been chosen it repeats
            return level_choice()
# TypeError: 'bool' object is not subscriptable

    def question_choice():
        global score
        score_num = 0
        answer = 0
        a = level_choice()  # defines the function while calling it
        categories_input = a[0]  # defines the category input from list
        level_input = a[1]  # defines the level input from list

        if categories_input == 1:  # prints ascii art for each category
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

        if level_input == 1:  # filters the questions based on there level then category
            if categories_input == 1:
                answer = "1"
                fish_list.append(1)  # states the corresponding answer and score value for the question
                score_num = 100
                try:
                    question1 = open("question 1.txt", "r")
                    line = question1.readlines()
                    print(line[4])
                    print(line[5])
                    print(line[6])
                    print(line[7])
                    print(line[8])
                except:
                    print("ERROR")
            elif categories_input == 2:
                answer = "1"
                cheese_list.append(1)
                score_num = 100
                try:
                    question1 = open("question 1.txt", "r")
                    line = question1.readlines()
                    print(line[30])
                    print(line[31])
                    print(line[32])
                    print(line[33])
                    print(line[34])
                except:
                    print("ERROR")
            elif categories_input == 3:
                answer = "1"
                lightbulbs_list.append(1)
                score_num = 100
                try:
                    question1 = open("question 1.txt", "r")
                    line = question1.readlines()
                    print(line[56])
                    print(line[57])
                    print(line[58])
                    print(line[59])
                    print(line[60])
                except:
                    print("ERROR")

        elif level_input == 2:
            if categories_input == 1:
                answer = "2"
                fish_list.append(2)
                score_num = 200
                try:
                    question1 = open("question 1.txt", "r")
                    line = question1.readlines()
                    print(line[12])
                    print(line[13])
                    print(line[14])
                    print(line[15])
                    print(line[16])
                except:
                    print("ERROR")
            elif categories_input == 2:
                answer = "2"
                cheese_list.append(2)
                score_num = 200
                try:
                    question1 = open("question 1.txt", "r")
                    line = question1.readlines()
                    print(line[38])
                    print(line[39])
                    print(line[40])
                    print(line[41])
                    print(line[42])
                except:
                    print("ERROR")
            elif categories_input == 3:
                answer = "2"
                lightbulbs_list.append(2)
                score_num = 200
                try:
                    question1 = open("question 1.txt", "r")
                    line = question1.readlines()
                    print(line[64])
                    print(line[65])
                    print(line[66])
                    print(line[67])
                    print(line[68])
                except:
                    print("ERROR")
        elif level_input == 3:
            if categories_input == 1:
                answer = "3"
                fish_list.append(3)
                score_num = 300
                try:
                    question1 = open("question 1.txt", "r")
                    line = question1.readlines()
                    print(line[20])
                    print(line[21])
                    print(line[22])
                    print(line[23])
                    print(line[24])
                except:
                    print("ERROR")
            elif categories_input == 2:
                answer = "3"
                cheese_list.append(3)
                score_num = 300
                try:
                    question1 = open("question 1.txt", "r")
                    line = question1.readlines()
                    print(line[46])
                    print(line[47])
                    print(line[48])
                    print(line[49])
                    print(line[50])
                except:
                    print("ERROR")
            elif categories_input == 3:
                answer = "3"
                lightbulbs_list.append(3)
                score_num = 300
                try:
                    question1 = open("question 1.txt", "r")
                    line = question1.readlines()
                    print(line[72])
                    print(line[73])
                    print(line[74])
                    print(line[75])
                    print(line[76])
                except:
                    print("ERROR")

        question_answer = input("1, 2, 3 or 4")  # input for your answer
        while question_answer != "1" and question_answer != "2" and question_answer != "3" and question_answer != "4":  # defencive coding
            print("error")
            question_answer = input("1, 2, 3 or 4")
        if question_answer == answer:  # option if correct
            score = score + score_num  # tells you your new score by adding the questions value to the score value
            print("correct! your score is now ", score)
        elif question_answer != answer:  # option if incorrect
            print("incorrect! your score is ", score)  # tells you your score


    while len(fish_list) < 3 or len(cheese_list) < 3 or len(lightbulbs_list) < 3:
        question_choice()  # repeats the function until all questions are answered

    print("you have answered all the questions")
    print(name, " your score is ", score)
    highscoreinput = input("would you like to save your score?  yes or no")  # option to save score
    while highscoreinput != "no" and highscoreinput != "yes":  # defencive coding
        print("error")
        highscoreinput = input("would you like to save your score?  yes or no")
    if highscoreinput == "no":
        break
    elif highscoreinput == "yes":
        try:
            f = open("savefile.txt", "a")  # appends your name and score to savefile.txt
            f.write("\n" + str(name) + ", " + str(score))
            f.close()
        except:
            print("ERROR")
        else:
            print("Success")  # tells you it was completed

    ending = input("do you want to restart: yes or no  ")  # code to restart the entire game
    while ending != "no" and ending != "yes":  # defencive coding
        print("error")
        ending = input("do you want to restart: yes or no  ")
    if ending == "no":
        restart = restart + 1
    elif ending == "yes":
        restart = restart + 0
