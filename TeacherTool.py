"""
Teacher Tool is a suite of useful tools for teachers.
These include a test generator at the moment.
"""
def choice_creator():
    """Ask for questions & answers and print the generated test"""
    # storage string for response choices
    multiple_choice = "abcdefg"

    # ask for number of questions to be filled out
    number_questions = int(input("How many multiple choice questions do you want?"))

    # ask for the number of answers per question
    choices_per_question = int(input("How many choices per question? (Max 7)\n>"))
    test = ""

    for i in range(number_questions):
        question = input("What is question number " + str(i+1) + "?\n>")
        test += str(i+1) + ". " + question + "\n"

        for j in range(choices_per_question):
            possible_answer = input("Type a possible answer.\n>")
            test += "  " + multiple_choice[j] + "." + possible_answer + "\n"

    print(test)

"""
MAIN
"""

# introduce the program
print("Hello! Welcome to TeacherTool. This is your one stop shop for all your teaching needs.\n"\
"type \"help\" for directions and possible commands.")

"""Begin inputs"""
while True:
    USER_CHOICE = str(input(">"))

    if USER_CHOICE == "exit":
        break

    elif USER_CHOICE == "help":
        print("List of possible commands: \n"\
        "To create a multiple choice test, type in \"Create multiple choice test\"\n")

    elif USER_CHOICE == "Create multiple choice test":
        choice_creator()

    else:
        print("Unknown command. type \"help\" for a list of commands")
