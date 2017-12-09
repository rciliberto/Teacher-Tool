from multiple_choice import MCTest, MCQuestion

test = MCTest()
test.set_name("Test test")
questions = []


q1 = MCQuestion()
q1.set_question("Hello")
q1.add_answer("hi", True)
#q1.add_answer("bye", False)
test.add_question(q1)

q2 = MCQuestion()
q2.set_question("Hello")
q2.add_answer("hi", True)
q2.add_answer("bye", False)
test.add_question(q2)

print(test)
