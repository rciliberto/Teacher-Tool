"""
Includes multiple choice test and question classes and related final static variables
"""
from docx import Document

class MCAnswer(object):
    """An answer object thet stores an answer string ans whether it is true or not"""

    def __init__(self, answer, is_correct):
        self.answer = answer
        self.is_correct = is_correct

    def __str__(self):
        return self.answer

class MCQuestion(object):
    """A question object that stores a question and its answers"""
    LETTERS = "abcdefg"

    def __init__(self):
        self.question = ""
        self.answers = []

    def __str__(self):
        output = "  " + self.question + "\n"
        for i in range(len(self.answers)):
            output += "     " + MCQuestion.LETTERS[i] + ". " + str(self.answers[i]) + "\n"
        return output

    def set_question(self, question):
        """sets the question"""
        self.question = str(question)

    def add_answer(self, answer, is_correct):
        """add an answer to the question"""
        self.answers.append(MCAnswer(answer, is_correct))

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

    def make_docx(self, doc_name):
        """Make a .docx document representation of the test"""
        doc = Document()
        doc.add_heading(self.test_name, 0)

        for i in range(len(self.questions)):
            doc.add_paragraph(str(i+1) + ". " + self.questions[i].question)

            for j in range(len(self.questions[i].answers)):
                doc.add_paragraph(" " + MCQuestion.LETTERS[j] + ". "\
                    "" + str(self.questions[i].answers[j]))

        doc.add_paragraph("")
        doc.save(doc_name + ".docx")

    def make_answer_key(self):
        """Make an answer key"""
        doc = Document()
        doc.add_heading(self.test_name + " Answers", 0)

        for i in range(len(self.questions)):
            question = self.questions[i]

            doc.add_paragraph(str(i+1) + ". " + question.question)
            for j in range(len(question.answers)):
                if question.answers[j].is_correct:
                    doc.add_paragraph(" " + MCQuestion.LETTERS[j] + ". "\
                        "" + str(question.answers[j]))

        doc.add_paragraph("")
        doc.save(self.test_name + "_ans.docx")
