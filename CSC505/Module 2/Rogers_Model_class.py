
class Rogers_Model:

    def __init__(self):
        self.current_selection = ""
        self.model = {
            "Communication": {
                "items": ["Project Initiation", "Requirement Gathering"],
                "next": ["Planning"]
            },
            "Planning": {
                "items": ["Estimating", "Scheduling", "Tracking"],
                "next": ["Modeling"]
            },
            "Modeling": {
                "items": ["Analysis", "Design"],
                "next": ["Prototyping"]
            },
            "Prototyping": {
                "items": ["Testing Feasibility of idea before diving into development of proposed product"],
                "next": ["Construction"]
            },
            "Construction": {
                "items": ["Code", "Test", "Peer Validation"],
                "next": ["Internal Testing/BETA"]
            },
            "Internal Testing/BETA": {
                "items": ["Test current code with stakeholders", "Determine current shortcomings", "Add features where necessary"],
                "next": ["Adjustments", "Construction"]
            },
            "Adjustments": {
                "items": ["Submit change request forms for core features"],
                "next": ["Construction"]
            },
            "Deployment": {
                "items": ["Delivery", "Support", "Feedback", "TAM"],
                "next": ["Next Feature Deployment"]
            },
        }


    def print_model(self, selection):
        print(f"---------------Key Feature: {selection}---------------\nKey Items of {selection}:")
        [print(f"- {i}") for i in self.model[selection]["items"]]

model = Rogers_Model()
while True:
    selection = input("Which key item would you like to see?\nChoices: Communication, Planning, Modeling, Prototyping, Construction, Internal Testing/BETA, Adjustments, Deployment, QUIT: ")
    if selection != "QUIT":
        try:
            model.model[selection]
            model.print_model(selection)
            print(f"{selection} leads into: ")
            [print(f"- {o}") for o in model.model[selection]["next"]]
            print(f"---------------END OF {selection}---------------")
        except:
            print("Unrecognized Key Feature Name.....Try Again!")
    else:
        break