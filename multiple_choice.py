"""
Includes multiple choice test and question classes and related final static variables
"""
from docx import Document

class MCQuestion(object):
    """A question object that stores a question and its answers"""
    LETTERS = "abcdefg"
    
    def __init__(self):
        self.question = ""
        self.answers = []
        self.correct_index = -1

    def __str__(self):
        output = "  " + self.question + "\n"
        for i in range(len(self.answers)):
            output += "     " + MCQuestion.LETTERS[i] + ". " + self.answers[i] + "\n"
        return output

    def set_question(self, question):
        """sets the question"""
        self.question = str(question)

    def add_answer(self, answer, is_correct):
        """add an answer to the question"""
        self.answers.append(answer)
        if is_correct:
            self.correct_index = len(self.answers)-1

class MCTest(object):
    """A test object that stores multiple questions"""

    def __init__(self):
        self.test_name = ""
        self.questions = []

    def __str__(self):
        output = self.test_name + "\n"
        for question in self.questions:
            output += str(question) + "\n"
        return output

    def add_question(self, question):
        """add a question to the test"""
        self.questions.append(question)

    def set_name(self, name):
        """Set the name of the test"""
        self.test_name = str(name)

    def make_docx(self):
        """Make a .docx document representation of the test"""
        doc = Document()
        doc.add_heading(self.test_name, 0)
        for i in range(len(self.questions)):
            doc.add_paragraph(str(i+1) + ". " + self.questions[i].question)

            for j in range(len(self.questions[i].answers)):
                doc.add_paragraph("  " + MCQuestion.LETTERS[j] + ". " + self.questions[i].answers[j])

        doc.add_paragraph("")
        doc.save(self.test_name + ".docx")
