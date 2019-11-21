my_dict = {}

# print(type(my_dict))

my_dict = {
    1:"orange",
    2:"bananas",
    3:"apples"
}
# accessing a value : call the key
vr = my_dict[1]
print(vr)


details = {
    "name":"joshua",
    "married": True,
    "age":10
}
# access joshua's age
print(details["age"])

details3 = {
    "name":"joshua",
    "dislikes":["lazy", "broke"],
    "parents": {
        "mother":"Nancy",
        "father":"Peter"
    }
}

# name of john's mom
newVar = details3["parents"]

#print(newVar["mother"])

# print(details3["parents"]["mother"])


# Determing type of variable in taskList using an inbuilt function

taskList = [23, "Jane", ["Lesson 23", 560, {"currency": "KES"}], 987, (76, "John")]
y = type(taskList)
print(y)

# Print KES

print(taskList[2][2]["currency"])



# Print 560

print(taskList[2][1])

# Use a function to determine the length of taksList

print(len(taskList))

# Change 987 to 789 without using an inbuilt -method or Assignment
print(str(taskList[3])[::-1])


# Change the name “John” to “Jane” .
print(taskList[4][1].replace("John", "Jane"))
# print(taskList)