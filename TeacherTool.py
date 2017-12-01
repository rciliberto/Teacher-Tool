print("Hello! Welcome to TeacherTool. This is your one stop shop for ")

def choiceCreator:

    numberquestions = int(input("How many multiple choice questions do you want?"))
    multiple_choice = "abcdefg"
    numbermultiplechoice = int(input("How many choices per question? (Max 7)"))
    iterator = 1
    finalstring = ""

    while (iterator != numberquestions + 1):
        iterator += 1
        question = input("What is your first question?")
        choicecounter = 0

        while (choicecounter < len(multiple_choice)):
            choice = multiple_choice[choicecounter]
            choicecounter += 1
