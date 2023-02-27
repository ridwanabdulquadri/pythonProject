class Credit_card_validator:
    def __init__(self, card_sum, card_validation, card_type):
        self.card_type = card_type
        self.card_validation = card_validation
        self.card_sum = card_sum

    def set_sum(self, card):
        self.card_sum = even_numbers_add(card) + add_odd_numbers(card)

    def set_card_validation(self, card):
        self.card_validation = validate_card_length(card)

    def get_card_validation(self):
        return self.card_validation

    def get_card_sum(self):
        return self.card_sum

    def set_card_type(self, card_number):
        if card_number[0] == "4":
            self.card_type = "VisaCard"
        elif card_number[0] == "5":
            self.card_type = "MasterCard"
        elif card_number[0] == "3" and card_number[1] == "7":
            self.card_type = "American Express Cards"
        elif card_number[0] == "6":
            self.card_type = "DiscoverCard"
        else:
            self.card_type = "Invalid card type"

    def get_card_type(self):
        return self.card_type
def validate_card_length (card_number):
    if len(card_number) < 13 or len(card_number) > 16:
        print("Invalid Card Number")
    else:
        print("Valid")

def even_numbers_add (card):
    sum_of_even_numbers =0
    for number in range(len(card)-2, -1, -2):
        sum_of_even_digits = (int(card[number]) * 2)
        if number > 9:
            newSum = (sum_of_even_digits % 10) + (sum_of_even_digits // 10)
            sum_of_even_numbers += newSum
        else:
            sum_of_even_numbers += sum_of_even_digits
        return sum_of_even_numbers

def add_odd_numbers(card_number):
    sum_of_odd_digit = 0
    for i in range(len(card_number) - 1, -1, -2):
        sum_of_odd_digit += int(card_number[i])
    return sum_of_odd_digit


#MAIN CLASS
if __name__ == '__main__':
    card_checker = Credit_card_validator(5, card_validation="valid", card_type="Master")

    card_detail = input("Enter Card Details: ")
    print("*************************************")
    print("****Card Number: ", card_detail)
    card_checker.set_sum(card_detail)
    card_checker.set_card_validation(card_detail)
    card_checker.set_card_type(card_detail)

    print("****Card length Validity: ", card_checker.get_card_validation())
    print("****Card Length: ", len(card_detail))
    if card_checker.get_card_sum() % 10 == 0:
        print("****Card Type: valid")
    else:
        print("****Card Type Validity: invalid")

    print("****Card Type: ", card_checker.get_card_type())
    print("*************************************")
