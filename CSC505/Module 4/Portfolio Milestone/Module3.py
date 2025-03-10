
class Rogers_Model:

    def __init__(self):
        self.current_selection = ""
        self.model = {
            "Screen_1": {
                "page": "Main Screen contains a scrolling list of lists. The user can create new lists or delete old ones.",
                "next": ["Screen_2", "Popup_choice", "Screen_3"]
            },
            "Screen_2": {
                "page": "Screen 2 contains a scrolling list of items with the name, item count, a checkbox and a remove. The user can also add new items from this screen.",
                "next": ["Screen_1", "Popup_choice", "Screen_4"]
            },
            "Screen_3": {
                "page": "Screen 3 is where the user can pick the date of the grocery trip as the name of the list.",
                "next": ["Screen_1"]
            },
            "Screen_4": {
                "page": "Screen 3 is where the user can enter the item name and item count for the grocery screen.",
                "next": ["Screen_2"]
            },
            "Popup_choice": {
                "page": "The choice popup is for making sure the user wants to delete the selected item.",
                "next": ["Current_Screen"]
            },
            "Popup_calendar": {
                "page": "The calendar popup is for selecting the current date easier than typing if the user wishes.",
                "next": ["Current_Screen"]
            },
        }


    def print_model(self, selection):
        print(f"---------------{selection}: ---------------")
        print(f"Description: {self.model[selection]["page"]}")
        print(f"{selection} leads into: ")
        [print(f"- {o}") for o in model.model[screen]["next"]]

model = Rogers_Model()
print(f"---------------Prototype Grocery List App---------------\n\n")
print(f"Number of Screens: {len(model.model)}")
for screen in model.model:
    model.print_model(screen)

