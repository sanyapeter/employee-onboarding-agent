from agent.knowledge import load_employee
from agent.assistant import respond

employee = load_employee()

while True:
    question = input(f"\n{employee['name']}: ")

    if question.lower() == "exit":
        break

    response = respond(question)

    print(f"\nAgent: {response}")