import json


def load_knowledge():
    with open("data/onboarding.json", "r") as file:
        return json.load(file)


def load_employee():
    with open("data/employees.json", "r") as file:
        return json.load(file)


def find_information(question):
    knowledge = load_knowledge()
    question = question.lower()

    for keyword, information in knowledge.items():
        if keyword in question:
            return information

    return None