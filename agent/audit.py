from datetime import datetime

def audit(employee, question, status):
    with open("audit.log", "a") as file:
        file.write(
            f"{datetime.now()} | "
            f"{employee} | "
            f"{status} | "
            f"{question}\n"
        )