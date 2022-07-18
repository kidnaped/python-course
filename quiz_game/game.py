# ----------------------------------
def new_game():
    guesses = []            # list of all guesses we made
    correct_guesses = 0     # score of our correct answers
    question_num = 0

    for key in questions:                                           # main game loop, where we print a key from dict one after another
        print("----------------------------------")                 # and compare it to our input guess
        print(key)                                                  # prints our question
        for i in options[question_num]:                             # prints the guesses to choose
            print (i)
        guess = input("Enter (A, B, C or D): ").upper()             # input our guess
        guesses.append(guess)                                       # place our guess in a list

        correct_guesses += check_answer(questions.get(key), guess)  # checks our guess and adds a score, 1st parameter in func is real answer from key value, second - our guess
        question_num += 1                                           # proceed to next question
    
    display_score(correct_guesses, guesses)                         # funcion that displays our score based on correct anwers

# ----------------------------------
def check_answer(answer, guess):                    # first param is the right answer from dict key value, sec - our guess
    if answer == guess:                             # compare two parameters
        print("CORRECT!")
        return 1                                    # return score to add in correct_guesses var
    else:
        print("WRONG!")
        return 0
# ----------------------------------
def display_score(correct_guesses, guesses):        # funcion that displays our score based on correct anwers
    print("----------------------------------")
    print("RESULTS")
    print("----------------------------------")
    
    print("Answers: ", end="")
    for i in questions:                             # diplays value for all keys in dict
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")                      #  diplay value of our guesses list 
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)   # score in % correct guesses divided by total questions
    print("Your score is:", str(score), "%")


# ----------------------------------
def play_again():                                      # funct that manages possible repeated play
    response = input("Do you want to play again? (Y/N) ").upper()

    if response == "Y":
        return True
    else:
        return False
# ----------------------------------

questions = {
    "Who created Python?: " : "A",
    "What year was Python created?: " : "B",
    "Python is tributed to which comedy group?: " : "C",
    "Is the Earth round?: " : "A"
}

options =   [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
            ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
            ["A. Lonely Island", "B. Smosh", "C. Monthy Python", "D. SNL"],
            ["A. True", "B. False", "C. Sometimes", "D. What's Earth?"]]

new_game()

while play_again():     # if func play_again returns True - starts a new game
    new_game()

print("BYE!")