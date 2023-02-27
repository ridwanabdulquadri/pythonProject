class User:
    def __init__(self, surname, name, other_name, address, date_of_birth, photo, state_of_origin, nationality,
                 card_number):
        self.surname = surname
        self.name = name
        self.other_name = other_name
        self.address = address
        self.date_of_birth = date_of_birth
        self.photo = photo
        self.state_of_origin = state_of_origin
        self.nationality = nationality
        self.card_number = card_number

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def set_surname(self, surname):
        self.surname = surname

    def get_other_name(self):
        return self.other_name

    def set_other_name(self, other_name):
        self.other_name = other_name

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_date_of_birth(self):
        return self.date_of_birth

    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth

    def get_photo(self):
        return self.photo

    def set_photo(self, photo):
        self.photo = photo

    def get_state_of_origin(self):
        return self.state_of_origin

    def set_state_of_origin(self, state_of_origin):
        self.state_of_origin = state_of_origin

    def get_nationality(self):
        return self.nationality

    def set_nationality(self, nationality):
        self.nationality = nationality

    def get_card_number(self):
        return self.card_number