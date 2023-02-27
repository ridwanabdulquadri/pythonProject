from itertools import count

if __name__ == '__main__':

    number = int(input("Enter a number: "))
    number2 = int(input("Enter a number: "))
    #
    # print(number + number2)
    # print(number2)

    if number > number2:
        print(f"{number} is greater")
    elif number2 > number:
        print(f"{number2} is greater")
    else:
        print(f"{number} is equals {number2}")
