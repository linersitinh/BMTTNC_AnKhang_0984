class Student:
    auto_id = 1

    def __init__(self, name, gender, major, gpa):
        self.id = Student.auto_id
        Student.auto_id += 1

        self.name = name
        self.gender = gender
        self.major = major
        self.gpa = gpa

    def get_academic_rank(self):
        if self.gpa >= 8:
            return "Gioi"
        elif self.gpa >= 6.5:
            return "Kha"
        elif self.gpa >= 5:
            return "Trung binh"
        else:
            return "Yeu"

    def __str__(self):
        return f"{self.id:<5}{self.name:<20}{self.gender:<10}{self.major:<20}{self.gpa:<10.2f}{self.get_academic_rank():<15}"