class Pugs(Dog):

    def make_sound(self, sound="Woof Woof"):
        return super().make_sound(sound)





cyn = Pugs("cynthia", 3)
print(cyn.make_sound())