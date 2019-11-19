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

print(details3["parents"]["mother"])

