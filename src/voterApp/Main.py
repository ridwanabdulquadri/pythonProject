from enum import Enum
from typing import List

class Party(Enum):
    LPC = 1
    APC = 2
    PDP = 3

class Voters:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.isEligible = age >= 18

voters = [
    Voters("Ridwan", 20),
    Voters("tunde", 25),
    Voters("ik", 16),
    Voters("Ayo", 30),
    Voters("John", 21),
    Voters("Sunday", 19)
]

print([v.name for v in voters])
print(f"we have {len(voters)} total number of voters")

parties = [Party.LPC, Party.PDP, Party.APC]
print([p.name for p in parties])
print(f"we have {len(parties)} parties registered")