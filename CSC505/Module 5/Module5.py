class PHTRS:
    def __init__(self):
        self.actors = {
            "Citizen": [
                "Report Pothole: Citizens can report potholes with location, size, and severity.",
                "View Pothole Status: Citizens can check the current status of reported potholes.",
                "Report Damage: Citizens can report any damage caused by potholes (e.g., to vehicles)."
            ],
            "Public Works Department Employee": [
                "Assign Priority to Potholes: Employees can assign a priority level to potholes based on their size.",
                "Create Work Orders: Employees can create work orders for repair crews.",
                "Track Repair Progress: Employees can monitor the progress of pothole repairs.",
                "Update Repair Status: Employees can update the status of the repair (e.g., in progress, repaired).",
                "Record Repair Costs: Employees record costs associated with the repair (e.g., labor, materials).",
                "View Pothole Reports: Employees can view all potholes reported and their details.",
                "Manage Damage Claims: Employees can manage claims reported by citizens regarding damages from potholes."
            ],
            "Repair Crew": [
                "Receive Work Orders: Repair crew receives assigned work orders to repair potholes.",
                "Update Repair Status: Crew can update the status of their repair (work in progress, completed).",
                "Log Repair Details: Crew logs hours worked, materials used, and other repair details."
            ],
            "System Administrator": [
                "Manage Users: Admin can manage user accounts (create, update, delete users).",
                "Configure System Settings: Admin can configure system-level settings.",
                "Ensure Data Integrity: Admin ensures data is accurate and consistent."
            ]
        }

        self.description = """
        The Pothole Tracking and Repair System (PHTRS) is an online system that allows citizens to report potholes and track their repair status.
        The system includes actors such as citizens, public works employees, repair crews, and system administrators. 
        Each actor has specific use cases that describe their interaction with the system.

        Actors:
        1. Citizen: Reports potholes and damage, views status.
        2. Public Works Department Employee: Manages potholes, assigns repair priorities, tracks repair status, and manages damage claims.
        3. Repair Crew: Receives and completes work orders, logs repair details.
        4. System Administrator: Manages users and system configuration.

        Use Cases:
        Each actor has a set of use cases that define their interaction with the system.
        """

    def print_description(self):
        print(self.description)

phtrs = PHTRS()
phtrs.print_description()
for actor, use_cases in phtrs.actors.items():
    print(f"Actor: {actor}")
    for use_case in use_cases:
        print(f" - {use_case}")
    print()

