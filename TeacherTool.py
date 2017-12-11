"""
Teacher Tool is a suite of useful tools for teachers.
These include a test generator at the moment.
"""
import os
import random

from multiple_choice import MCQuestion, MCTest


def clear():
    """Clear terminal window depending on OS"""
    # windows
    if os.name == "nt":
        os.system("cls")
    # UNIX/MacOS
    elif os.name == "posix":
        os.system("clear")

def choice_creator(test):
    """Ask for questions & answers and print the generated test"""
    # creates a test document
    test = MCTest()

    # ask for a test name and add it to the doc
    test_name = input("What is the name of your test?\n> ")
    test.set_name(test_name)

    # ask for number of copies
    num_copies = -1
    while num_copies < 0:
        try:
            num_copies = int(input("How many forms do you want?\n> "))
        except:
            print("You must enter a positive number. Try again:\n")

    # ask for number of questions to be filled out
    number_questions = -1
    while number_questions < 0:
        try:
            number_questions = int(input("\nHow many multiple choice questions do you want?\n> "))
        except:
            print("You must enter a positive number. Try again:\n")

    # ask for the number of answers per question
    choices_per_question = -1
    while choices_per_question < 0 or choices_per_question > 7:
        try:
            choices_per_question = int(input("\nHow many choices per question? (Max 7)\n> "))
        except:
            print("You must enter a positive number less than or equal to 7. Try again:")

    for i in range(number_questions):
        # ask for the question
        question = MCQuestion()
        quest = input("\nWhat is question number " + str(i+1) + "?\n> ")
        question.set_question(quest)

        # ask for the correct answer
        correct = input("\nWhat is the correct answer?\n> ")
        question.add_answer(correct, True)

        # ask for answers
        for j in range(choices_per_question-1):
            ans = input("\nType a possible answer.\n> ")
            question.add_answer(ans, False)

        test.add_question(question)

    # make .docx files
    if num_copies > 1:
        for i in range(num_copies):
            new_name = test.test_name + " Form " + str(i+1)
            scrambled_test = scrambler(test, new_name)

            scrambled_test.make_docx(new_name)
            scrambled_test.make_answer_key()
    else:
        doc_name = test.test_name + "_MASTER"
        scrambled_test = scrambler(test, test.test_name)
        scrambled_test.make_docx(doc_name)
        scrambled_test.make_answer_key()

    print("Sucessfully Created test!")

def scrambler(original_test, new_name):
    """scrambles both the questions and the answers for each question when a test is given"""
    new_test = MCTest()

    for question in original_test.questions:
        new_index = random.randint(0, len(new_test.questions))
        new_test.questions.insert(new_index, question)

    for question in new_test.questions:
        temp = []
        for i in range(len(question.answers)):
            new_index = random.randint(0, len(temp))
            temp.insert(new_index, question.answers[i])
        question.answers = temp

    new_test.test_name = new_name

    return new_test

"""
MAIN
"""

clear()
# introduce the program
print("Hello! Welcome to TeacherTool. This is your one stop shop for all your teaching needs.\n"\
"type \"help\" for directions and possible commands.")

# global MCTest variable
MC_TEST = MCTest()

# begin inputs
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
        choice_creator(MC_TEST)
    else:
        print("Unknown command. type \"help\" for a list of commands")
