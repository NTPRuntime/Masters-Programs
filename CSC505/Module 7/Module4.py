
class UMLFramework:
    def __init__(self):
        self.description = "This program outlines the traits, and supporting skills and practices of an \n" \
        "excellent software developer based on personal experiences and observations."
        self.components = {
            "Traits": ["Creativity", "Persistence", "Collaboration"],
            "Skills": ["Problem Solving", "Algorithmic Design", "Debugging", "Optimization", "Time Management", 
                       {"Productivity": ["Focus", "Ability to change directions (Agile setting)", "Task Automation"],}],
            "Tools": ["Version Control", "Language Versatility", "Frameworks and Supporting Software"],
            "Work Practices": ["Knowledge on different development methodologies", "Code Reviews", "Stakeholder Interaction", "Peer Programming", 
                               {"Quality": ["Unit Teseting", "Good Comments", "Code Organization"]}],
        }

    def print_description(self):
        print(f"Description: {self.description}")

    def print_dependencies(self, item:dict):
        for key, values in item.items():
            print(f"  - {key}: {len(values)} items")
            for value in values:
                if type(value) == str:
                    print(f"    * {value}")

    def print_components(self):
        print("\nImportant Steps and Components:")
        for key, values in self.components.items():
            print(f"- {key}: {len(values)} items")
            for value in values:
                if type(value) == str:
                    print(f"  * {value}")
                else:
                    self.print_dependencies(value)

if __name__ == "__main__":
    uml_framework = UMLFramework()
    uml_framework.print_description()
    uml_framework.print_components()