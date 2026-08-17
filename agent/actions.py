def create_access_request(employee, system):
    return {
        "status": "created",
        "employee": employee,
        "system": system,
        "ticket": "ONB-1001"
    }