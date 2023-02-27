# def find_divisors():
#    user_input = int(input("Enter a number: "))
#    divisors = []
#    for i in range(1, user_input + 1):
#        if user_input % i == 0:
#            divisors.append(i)
#    print(f"The divisors of {user_input} are: {divisors}")
# find_divisors()


# Given two lists, Write a function that returns a list that contains only the elements that are common
# between the lists without duplicates. Make sure your program works on two lists of different sizes.
# def two_common_elements(list1, list2):
#    return list(set(list1) & set(list2))
# list1 = [1, 2, 3, 4, 5, 7, 8]
# list2 = [2, 4, 6, 8, 10]
# print(two_common_elements(list1, list2))
# ALTERNATIVE
def common_elements(list1, list2):
    common = []
    for element in list1:
        if element in list2 and element not in common:
            common.append(element)
    return common


list1 = [1, 2, 3, 4, 5, 7, 8]
list2 = [2, 4, 6, 8, 10]
print(common_elements(list1, list2))

print([x for x in list1 if x in list2])
