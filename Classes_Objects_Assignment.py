#Student
#School name = ABC PRIMARY SCHOOL
#Class 5
#Name, Marks for English, Math, Kiswahili, Science, SST
#Method I) To find Total Marks
#       II) To find Average Score
#       III) To grade the student

class Student():
    school_name = "ABC Primary School"
    levelClass = "5"
    avg = 0
    total = 0
    def __init__(self, Eng, Math, Kiswahili, Science, SST):
        self.Eng = Eng
        self.Math = Math
        self.Kiswahili = Kiswahili
        self.Science = Science
        self.SST = SST

    def totalMarks(self):
        totalmarks = self.Eng + self.Kiswahili + self.Math +self.Science + self.SST
        self.total = totalmarks
        return self.total

    def averageScore(self):
        average = (self.Eng + self.Kiswahili + self.Math +self.Science + self.SST)/5
        self.avg = average
        return self.avg

    def grade(self):

        if self.avg >= 79:
            return("Grade: A")
        elif self.avg >= 60:
            return("Grade: B")
        elif self.avg >= 49:
            return("Grade C")
        elif self.avg >= 40:
            return("Grade D")
        elif self.avg >= 0:
            return("E")
        else:
            return("Grade: Invalid")



julius = Student(78, 87, 76, 100, 89)
print(julius.totalMarks())
print(julius.averageScore())
print(julius.grade())

maria = Student(67, 76, 75, 74.4, 65)
print(maria.totalMarks())
print(maria.averageScore())
print(maria.grade())




