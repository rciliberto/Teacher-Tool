# this creates a multiple choice test.
def choiceCreator():
    # storage string for response choices
    multiple_choice = "abcdefg"

    questionNum = int(input("How many multiple choice questions do you want? "))

    choicesPerQuestion = int(input("How many choices per question? (Max 7) "))
    finalstring = ""

    for i in range(questionNum):
        question = input("What is question number " + str(i+1) + "?")
        finalstring += str(i+1) + ". " + question + "\n"

        for j in range(choicesPerQuestion):
            possibleAnswer = input("Type a possible answer.")
            finalstring += multiple_choice[j+1] + "." + possibleAnswer + "\n"

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
