from agent.knowledge import find_information, load_employee
from agent.policy import check_request
from agent.actions import create_access_request
from agent.audit import audit


def respond(question):

    # Load employee information
    employee_info = load_employee()

    employee = employee_info["name"]
    department = employee_info["department"]
    role = employee_info["role"]

    # Step 1: Check if request is sensitive
    policy = check_request(question)

    if policy == "ESCALATE":
        audit(employee, question, "escalated")

        return (
            f"Hi {employee}, this request requires additional authorization. "
            "I cannot complete it automatically, so I have escalated it "
            "to HR/IT."
        )

    # Step 2: Search company knowledge
    information = find_information(question)

    if information is None:
        audit(employee, question, "not_found")

        return (
            f"Sorry {employee}, I couldn't find that information in the "
            "onboarding knowledge base. Please contact HR or IT."
        )

    # Step 3: Check if an action is needed
    if information["action"] == "github_access":

        result = create_access_request(
            employee,
            "GitHub"
        )

        audit(employee, question, result["status"])

        return (
            f"Hi {employee}, {information['answer']} "
            f"I created access request {result['ticket']} for you."
        )

    # Step 4: Just provide information
    audit(employee, question, "answered")

    return f"Hi {employee}, {information['answer']}"