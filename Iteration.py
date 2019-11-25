"""
Two types:
1. For
2. While
"""

"""
1. FOR
#  - Checks for a condition and if the condition is true, it gives an output until the condition is False.

E.g
"""

list = [1, 2, 3, 4, 5]

name = "Valentine"

# for name in name:
#     print("the first letter is", name)

    # COUNTER
counter = 1
for name in name:
    print("Element ", counter, "=", name)
    counter+=1

marks = [50, 70, 80, 88, 90]

# TotalMarks = sum(marks)
# print(TotalMarks)

totalmarks = 0

for each in marks:
    totalmarks = totalmarks + each
# print(totalmarks)


"""
2. WHILE LOOP

-Used for definite ranges.
-Begins with the key word
    while test expression:
        Block of Code.
        
-The block of code can only be executed if the test expression is true.

"""

# while True:
#     print("Naibei")

# while range(0, 20):
#     print(0)

i = 1
# while i <= len(range(0, 10)):
#     print(i)
#     i = i + 1

# Write a program that prints your name 100 times.

i = 0
while i < 101:
    print("Miss_Naibei")
    i = i+1


# Write a program that outputs 100 lines, numbered 1 to 100, each with your name on it. The output should look like the output below.

i = 0
while i < len(range(0, 100)):
    i = i + 1
   # print(i, "your name")
#

for item in len(range(0,100)):



# Write a program that uses a for loop to print the numbers 8, 11, 14, 17, 20, . . . , 83, 86, 89.




