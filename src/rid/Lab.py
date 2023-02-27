muscles = [6, 2, 75, 5, 9, 1, 4, 50, 26, 13, 3]
new_list = []
for element in muscles:
    if element < 5:
        new_list.append(element)
print(new_list)

#Write this in one line of Python
print([element for element in muscles if element < 5])

#Ask the user for a number and return a list that contains only elements from the original-
#list that are smaller than that number given by the user.
asked_num = int(input("Enter a number: "))
reconfigured_list = []
for element in muscles:
    if element < asked_num:
        reconfigured_list.append(element)
print(reconfigured_list)