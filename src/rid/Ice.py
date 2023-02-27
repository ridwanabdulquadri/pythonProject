if __name__ == '__main__':

 def odd_or_even():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")
 print(odd_or_even())

# check if the number is a multiple of 4
def multiple_of_4():
    num = int(input("Enter a number: "))
    if num % 4 == 0:
        print(f"The number {num} is a multiple of 4.")
    else:
        print(f"The number {num} is not a multiple of 4.")
print(multiple_of_4())

#divider check
user_number = int(input("Enter a number: "))
checker = int(input("Enter a number to divide by: "))

if user_number % checker == 0:
    print(f"{user_number} is divisible by {checker}.")
else:
    print(f"{user_number} is not divisible by {checker}.")
