class Human():
    def __init__(self,name):
        print("Human created")
        self.name=name
    def type(self):
        print('Type of human is male or female')
    def living(self):
        print("Humans are living beings")


class Student(Human):
    def __init__(self,name,school):
        #Human.__init__(self,name)
        super().__init__(name)
        self.school=school
        print("Student Created")
    def type(self):
        print("Student is always a learner")

s=Student('Parth','SJS')
s.type()
s.living()
print(s.name)
print(s.school)
print(help(Student))