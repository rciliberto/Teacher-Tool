"""
Teacher Tool is a suite of useful tools for teachers.
These include a test generator at the moment.
"""
import os
from docx import Document
from docx.shared import Inches

def clear():
    """Clear terminal window depending on OS"""
    # windows
    if os.name == "nt":
        os.system("cls")
    # UNIX/MacOS
    elif os.name == "posix":
        os.system("clear")

def choice_creator():
    """Ask for questions & answers and print the generated test"""
    # creates a test document
    test = Document()

    # ask for a test name and add it to the doc
    test_name = input("What is the name of your test?\n> ")
    test.add_heading(test_name, 0)

    # storage string for response choices
    multiple_choice = "abcdefg"

    # ask for number of questions to be filled out
    number_questions = int(input("\nHow many multiple choice questions do you want?\n> "))

    # ask for the number of answers per question
    choices_per_question = int(input("\nHow many choices per question? (Max 7)\n> "))
    #test = ""

    for i in range(number_questions):
        question = input("\nWhat is question number " + str(i+1) + "?\n> ")
        test.add_paragraph(str(i+1) + ". " + question)

        for j in range(choices_per_question):
            possible_answer = input("\nType a possible answer.\n> ")
            test.add_paragraph("\n  " + multiple_choice[j] + ". " + possible_answer + "\n")

    test.save(test_name + ".docx")

"""
MAIN
"""

clear()
# introduce the program
print("Hello! Welcome to TeacherTool. This is your one stop shop for all your teaching needs.\n"\
"type \"help\" for directions and possible commands.")

#Begin inputs
while True:
    USER_CHOICE = str(input("> "))

    if USER_CHOICE.upper() == "EXIT":
        break
    elif USER_CHOICE.upper() == "HELP":
        print("\nList of possible commands: \n"\
        "CLEAR      -   Clear the screen\n"\
        "EXIT       -   Exit TeacherTool\n"\
        "HELP       -   Present this list of commands\n"\
        "\n"\
        "1          -   Make a multiple choice test\"\n")

    elif USER_CHOICE.upper() == "CLEAR":
        clear()
    elif USER_CHOICE.upper() == "1":
        choice_creator()

    else:
        print("Unknown command. type \"help\" for a list of commands")
