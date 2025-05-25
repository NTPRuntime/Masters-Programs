class ATM:
    def __init__(self):
        self.sequence = {
            "AuthenticateUser": {
                "description": "The user must authenticate using their PIN before they can access their account via the ATM.",
                "next": ["VerifyPin"],
                "retry": "None",
                "step": "1"
            },
            "VerifyPin": {
                "description": "The user must provide their correct PIN to access their account.",
                "next": ["VerifyPin", "RejectUser", "ViewBalance", "WithdrawMoney"],
                "retry": "if the pin is incorrect, try again until the user is verified before the third attempt or rejected after the third attempt.",
                "step": "2"
            },  
            "ViewBalance": {
                "description": "The user can view their current balance.",
                "next": ["EndInteraction"],
                "retry": "None",
                "step": "3"
            },
            "WithdrawMoney": {
                "description": "The user can withdraw from their account once verified.",
                "next": ["EnterAmount"],
                "retry": "None",
                "step": "4"
            },  
            "RejectUser": {
                "description": "The user is rejected after the third wrong PIN entry.",
                "next": ["EndInteraction"],
                "retry": "None",
                "step": "5"
            },
            "EnterAmount": {
                "description": "The user can enter an amount to be withdrawn.",
                "next": ["EnterAmount", "CheckBalance"],
                "retry": "if the amount is incorrect, try again using an amount divisible by 1, 5, or 10.",
                "step": "6"
            },
            "CheckBalance": {
                "description": "Their withdrawal amount is checked against their current balance. If the amount can be withdrawn then the interaction ends, otherwise the user is prompted to enter a different amount.",
                "next": ["CheckBalance", "CloseAccount", "EndInteraction"],
                "retry": "if there isnt enough money in the account, try again using a different amount.",
                "step": "7"
            },
            "CloseAccount": {
                "description": "If no money exists in the account then the account is closed.",
                "next": ["EndInteraction"],
                "retry": "None",
                "step": "8"
            },
            "EndInteraction" : {
                "description": "The end of the interaction with the user and the card is returned to them.",
                "next": ["ReturnCard"],
                "retry": "None",
                "step": "9"
            },
        }
        self.print_UML()

    def print_UML(self):
        for step in self.sequence:
            print(f"-----Step {self.sequence[step]["step"]}: {step}-----")
            print(f"\tDescription: {self.sequence[step]['description']}")
            for substep in self.sequence[step]['next']:
                try:
                    print(f"\t\t- Next Possible Step: {self.sequence[substep]['step']} - {substep}")
                except:
                    pass
            if self.sequence[step]['retry'] != "None":
                print(f"\tStep is retried {self.sequence[step]['retry']}")
                print("\n")
            else:
                print("\n")
            
ATM()