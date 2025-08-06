class Student:
    def __init__(self,name, matricule, gpa, Gender):
        # initializing the properties of the class
        self.name =name
        self.matricule = matricule
        self.gpa=gpa
        self.Gender = Gender
        def take_lesson(self):
            print(f"{self.name} is having {self.matricule}")
        def rank_student(self):
            for student in self.Student:
                if self.gpa>3.6:
                    print(f"{self.name} has {self.gpa} and graduate with firts class")

#Creating instance/objects of the student classs
first_student= Student("Blaise", "UBa22S0583", 3.5, "Male" )
second_student=Student("Salla-Nita", "UBa22S0552", 4.5, "Female")
print(f"The firt student is: {first_student.name}")