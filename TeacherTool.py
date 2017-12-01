# this creates a multiple choice test.
def choiceCreator():
    # storage string for response choices
    multiple_choice = "abcdefg"

    # ask for number of questions to be filled out
    questionNum = int(input("How many multiple choice questions do you want? "))

    # ask for the number of answers per question
    choicesPerQuestion = int(input("How many choices per question? (Max 7) "))
    test = ""

    for i in range(questionNum):
        question = input("What is question number " + str(i+1) + "?")
        test += str(i+1) + ". " + question + "\n"

        for j in range(choicesPerQuestion):
            possibleAnswer = input("Type a possible answer.")
            test += multiple_choice[j+1] + "." + possibleAnswer + "\n"

    print(test)

##########
## Main ##
##########

# introduce the program and ask for user input
print("Hello! Welcome to TeacherTool. This is your one stop shop for all your teaching needs.\ntype \"help\" for directions and possible commands.")
user_choice = input("What do you want to do?\n")

# possible actions user can do
if user_choice == "help":
    print("List of possible commands: \nTo create a multiple choice test, type in \"Create multiple choice test\"\n")

if user_choice == "Create multiple choice test":
    choiceCreator()
