"""
Includes multiple choice test and question classes and related final static variables
"""
LETTERS = "abcdefg"

class MCQuestion:
    """A question object that stores a question and its answers"""

    question = ""
    answers = []

    def __init__(self, question):
        self.question = question

    def __repr__(self):
        output = self.question + "\n"
        for i in self.answers:
            output += LETTERS[i] + ". " + self.answers[i] + "\n"
        return output

    def add_answer(self, answer):
        """add an answer to the question"""
        self.answers.append(answer)

class MCTest:
    """A test object that stores multiple questions"""

    test_name = ""
    questions = []

    def __init__(self, name):
        self.test_name = name

    def __repr__(self):
        for question in self.questions:
            print(question + "\n")

    def add_question(self, question):
        """add a question to the test"""
        self.questions.append(question)
