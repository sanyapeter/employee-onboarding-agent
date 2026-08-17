SENSITIVE_REQUESTS = [
    "admin access",
    "production access",
    "administrator",
    "delete employee",
    "payroll access"
]

def check_request(question):  # security check for highly sensitive information
    question = question.lower()

    for sensitive in SENSITIVE_REQUESTS:
        if sensitive in question:
            return "ESCALATE"

    return "ALLOW"