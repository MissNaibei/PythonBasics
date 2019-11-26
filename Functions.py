def add_two_numbers (a,b):
    sum = a + b
    return sum

add_two_numbers(30, 10)

# ans = add_two_numbers(30, 10)
# print(ans)


# QUESTION You've got chickens (2 legs), cows (4 legs) and pigs (4 legs) on your farm. Return the total number of legs on your farm. (CREATE A FUNCTION)

"""
a is the number of chicken
b is the number of cow
c is the number of pigs"""

def animals(chicken,cows,pigs):
    total_legs = 2 * chicken + 4 * cows + 4 * pigs
    return total_legs

# print(animals(2, 3, 5))
# print(animals(1, 2, 3))
# print(animals(5, 2, 8))

"""
Create a function that takes a list of numbers. Return the largest number in the list.
"""

def largestNumber (a, b,c, d):
    largest = max (a, b, c, d)
    return largest

# print(largestNumber(4, 5, 1, 3))
# print(largestNumber(300, 200, 600, 15))
# print(largestNumber(1000, 1001, 857, 1))

"""
Given a list of integers, return the difference between the largest and smallest integers in the list.
"""

def difference (aList):
    largest = max(aList)
    smallest = min(aList)
    diff = largest - smallest
    return diff

change = difference([10, 15, 20, 2, 10, 6])
# print(change)
change = difference([-3, 4, -9, -1, -2, 15])
# print(change)



"""
Create a function to concatenate two integer lists.
"""

def concatinate_Integers(List1, list2):
    joint = List1 + list2
    return joint

joint_List = concatinate_Integers([1, 3, 5], [2, 6, 8])
# print(joint_List)

joint_List = concatinate_Integers([7, 8], [10, 9, 1, 1, 2])
# print(joint_List)

joint_List = concatinate_Integers([4, 5, 1], [3, 3, 3, 3, 3])
# print(joint_List)

"""
Create a function that takes two strings as arguments and return either True or False depending on whether the total 
number of characters in the first string is equal to the total number of characters in the second string.
"""

def arguments (str1, str2):
    if len(str1) == len(str2):
        return "True"
    else:
        return "False"

# print(arguments("AB","CD"))
# print(arguments("ABC", "DE"))
# print(arguments("hello", "edabit"))

"""
Write a function that converts a dictionary into a list, where each element represents a key-value pair.
"""

#     list_key_value = [[k, v] for k, v in aDict.items()]
#     return list_key_value
#
# print(convert_to_array({ "a": 1, "b": 2 }))
# print(convert_to_array({ "shrimp": 15, "tots": 12 }))
# print(convert_to_array({}))

aDict = {"a": 1, "b": 2}



for each in aDict.items():
    # print(each)
    c = list(each)
    # print(c)
    # print(list(c.append(each))




"""
You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product. You 
are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars), and the 
starting inventory. Return the total profit made, rounded to the nearest dollar. Assume all of the inventory has 
been sold.
"""

def profit(aDict):
    cost = aDict["cost_price"]
    selling = aDict["sell_price"]
    stock = aDict["inventory"]
    gains = str(selling*stock - cost*stock)
    return gains
print(gains)

profit({
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
})
