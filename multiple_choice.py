"""
Includes multiple choice test and question classes and related final static variables
"""
LETTERS = "abcdefg"

class MCQuestion:
    """A question object that stores a question and its answers"""

    question = ""
    answers = []
    correct_index = -1

    def __repr__(self):
        output = self.question + "\n"
        for i in self.answers:
            output += LETTERS[i] + ". " + self.answers[i] + "\n"
        return output

    def set_question(self, question):
        """sets the question"""
        self.question = str(question)

    def add_answer(self, answer, is_correct):
        """add an answer to the question"""
        self.answers.append(answer)
        if is_correct:
            self.correct_index = len(self.answers)-1

class MCTest:
    """A test object that stores multiple questions"""

    test_name = ""
    questions = []

    def __repr__(self):
        for question in self.questions:
            print(question + "\n")

    def add_question(self, question):
        """add a question to the test"""
        self.questions.append(question)

    def set_name(self, name):
        """Set the name of the test"""
        self.test_name = str(name)
