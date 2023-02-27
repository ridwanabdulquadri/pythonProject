class Voters:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        if age >= 18:
            self.isEligible = True
        else:
            self.isEligible = False
        self.party = None