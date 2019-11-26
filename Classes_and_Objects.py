name = "Naibei"
age = 16
# print(type)
# print(type(name))
# print(type(age))


class Person:
    #class attribute - shared by all instances
    species = "Homo sapien"
#METHOD - Is a function defined inside a class. Self is a default parameter
    def walk(self):
        print("is walking.")
    def sleep(self):
        print("{} is sleeping.".format(self.jina))
    def __init__(self,name, age):
        print("I am the constructor method.")
        self.jina = name
        self.miaka = age

p6 = Person("Bev", 16)
p7 = Person("Maria", 54)

print(p6.jina)
print(p7.miaka)

p7.sleep()



# p1 = Person()
# p2 = Person()
# p3 = Person()
# p4 = Person()
#
# # print(p1)
# # print(p1.species)
#
#
# #ASSIGN P1 A NAME - instance attributes
#
# p1.name = "Price"
# p2.name = "Soraya"
# p1.age = 67
# print(p1.age)
# p1.race = "African_american"
# p1.nationality = "Rwandese"
# p1.city = "Nairobi"
# p1.spouse = "Alejandro"
#
# # print(p1.race)
# # print(p1.nationality)
# # print(p1.city)
# # print(p1.spouse)
#
# p1.walk()
# p1.sleep()
# p2.sleep()


# class Vehicle:
#      #class attribute - shared by all instances
#     brand = "Ford"
# # METHOD - Is a function defined inside a class. Self is a default parameter
#     def make(self):
#          print("is a Mustang.")
#     def year(self):
#          print("{} was manufactured in 1967.".format(self.owner))
#     def breakdown(self):
#          print("{} was towed to the garage down town.".format(self.owner))

# car_one = Vehicle()
# car_one.owner = "Miss_Naibei's Machine"
# print(car_one.brand)
# car_one.year()
# car_one.breakdown()





