# this creates a multiple choice test.
def choiceCreator():
    # storage string for response choices
    multiple_choice = "abcdefg"


    questionNum = int(input("How many multiple choice questions do you want? "))

    choicePerQuestion = int(input("How many choices per question? (Max 7) "))
    iterator = 1
    finalstring = ""

    for i in range(questionNum):
        question = input("What is question number " + str(iterator) + "?")
        finalstring += str(iterator) + ". " + question + "\n"
        choicecounter = 0

        # this nested while loop cycles through the possible choices for the question it applies to.
        while (choicecounter < choicePerQuestion):
            possibleAnswer = input("Type a possible answer.")
            finalstring += multiple_choice[choicecounter] + "." + possibleAnswer + "\n"
            choicecounter += 1

        iterator += 1

    print(finalstring)
    # this while loop cycles through for each question.
    # while (iterator != questionNum + 1):
    #     question = input("What is question number " + str(iterator) + "?")
    #     finalstring += str(iterator) + ". " + question + "\n"
    #     choicecounter = 0
    #
    #     # this nested while loop cycles through the possible choices for the question it applies to.
    #     while (choicecounter < choicePerQuestion):
    #         possibleAnswer = input("Type a possible answer.")
    #         finalstring += multiple_choice[choicecounter] + "." + possibleAnswer + "\n"
    #         choicecounter += 1
    #
    #     iterator += 1

    print(finalstring)

# intro
print("Hello! Welcome to TeacherTool. This is your one stop shop for (type in \"help\" for directions and possible commands).")
user_choice = input("What do you want to do?\n")

# possible actions user can do
if (user_choice) == "help":
    print("List of possible commands: \nTo create a multiple choice test, type in \"Create multiple choice test\"\nTo create ")

if (user_choice) == "Create multiple choice test":
    choiceCreator()

testAnswers = []
