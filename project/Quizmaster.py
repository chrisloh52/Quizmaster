#importing and setting variables so that they are seen by everything
import time
import random
questions = 10
sportQuestion = ''
sportAnswer = ''
score = 0
#intro and rules
print("Welcome to Quizmaster!\n\nThe goal of the game is to answer as many questions as you can.\nYou will choose from "
      "one of the two categories. There are 10 questions per category.\n\nRules:\n- You must answer each question word"
      " for word\n- If the answer has a number, type that number using letters\n- Don't cheat because that's not nice"
      "\n- You have as much time as you want to answer each question\n- Have fun!")

time.sleep(1)
#name for the end highscore
name = input("\nWhat is your name?")
playing = True
#while loop so that I can stop the game or the player can play again.
while playing:
    category = input("\nWhat category would you like to choose? Enter either 1 or 2.\n1. General Sports\n2. General "
                     "Geography\n")
    if category == '1':
        #try except to make sure there aren't any errors
        try:
            sportsQuestion = open("Sports_Category_Questions.txt", 'r')
            sportsAnswer = open("Sports_Category_Answers.txt", 'r')
            #opening files so they can be read

        except IOError:
            print("We are sorry, it seems we have gotten an error. Please contact us for assistance")
        questions = sportsQuestion.readlines()
        answers = sportsAnswer.readlines()
        #when questions or answers is called, they read the line they are on
        n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(n)
        #shuffle the line that is being read so that it is more game-like
        for i in n:
            #the player inputs the question and it is converted to lowercase
            #for loop makes it so the questions are all read before it moves on
            answer_entered = input(questions[i])
            answer_entered = answer_entered.lower()
            #remove all the leading and trailing spaces from the string
            if answer_entered == answers[i].strip():
                print("Correct")
                score = score + 1
                #add 1 to the score if correct
            elif answer_entered != answers[i].strip():
                print("Incorrect")
        #converts score to string and opens the highscorelist to append
        score = str(score)
        highscores = open("highscorelistsports.txt", 'a')
        #adds a new score to the highscore file
        highscores.write('\n' + name + "Score:" + score + "/10")
        highscores.close()
        #read all the highscores and print them
        highscores = open("highscorelistsports.txt", 'r')
        print("Highscores ", highscores.read())
        #ask if they want to try again
        print("Would you like to try again?")
        finish_or_tryagain = input("\n1. Yes, try again\n2. No, leave game")
        if finish_or_tryagain == '1':
            #playing = True means it redos the for loop
            playing = True
        elif finish_or_tryagain == '2':
            break
#Everything is repeating, only with geography questions
    elif category == '2':
        try:
            geographyQuestion = open("Geography_Category_Questions.txt", 'r')
            geographyAnswer = open("Geography_Category_Answers.txt", 'r')

        except IOError:
            print("We are sorry, it seems we have gotten an error. Please contact us for assistance")
        questions = geographyQuestion.readlines()
        answers = geographyAnswer.readlines()
        n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(n)
        for i in n:
            answer_entered = input(questions[i])
            answer_entered = answer_entered.lower()
            if answer_entered == answers[i].strip():
                print("Correct")
                score = score + 1
            elif answer_entered != answers[i].strip():
                print("Incorrect")
        score = str(score)
        highscores = open("highscorelistgeography.txt", 'a')
        highscores.write('\n' + name + "Score:" + score + "/10")
        highscores.close()
        highscores = open("highscorelistgeography.txt", 'r')
        print("Highscores ", highscores.read())
        print("Would you like to try again?")
        finish_or_tryagain = input("\n1. Yes, try again\n2. No, leave game")
        if finish_or_tryagain == '1':
            playing = True
        elif finish_or_tryagain == '2':
            break
    else:
        print("Wrong input, please try again.")
        time.sleep(5)










