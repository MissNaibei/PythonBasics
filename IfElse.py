"""
if... else statements in Python
syntax:
If test_expression:
    //statements

"""

# IF
# number = 100
# if number > 150:
#     print("I am ok.")


# IF...ELSE
# if number > 150:
#     print("I am ok.")
# else:print("I am not ok.")

# IF...ELIF
num = 20

if num > 0:
    print("{} is > than 0".format(num))

elif num ==10:
    print("{}is == to 10".format(num))
else:
    print("{} is a negative number".format(num))

# Create a program to ask for student's name , ask for marks for 5 subjects (Maths, Eng, Kiswahili, Scie, SST)

Name = input("Enter student name:")
English = int(input("Enter marks for English:"))
if English < 0 or English>100:
    print("Incorrect")
Kis = int(input("Enter marks for Kiswahili:"))
Math = int(input("Enter marks for Math:"))
Scie = int(input("Enter marks for Science:"))
SST = int(input("Enter marks for SST:"))

# TOTAL

total_score = English + Kis + Math + Scie + SST
print(total_score)


Average = total_score/5
print(Average)

if Average >= 79:
    print("A")
elif Average >= 60:
    print("Grade: B")
elif Average >= 49:
    print("Grade C")
elif Average >=40:
    print("Grade D")
elif Average>=0:
    print("E")
else:
    print("Grade: Invalid")


if 0<Average<10:
    print("random")