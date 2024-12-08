class Student :
    def __init__(self, name, gender, age, id, gpa) :
        self.name = name
        self.gender = gender
        self.age = age
        self.id = id
        self.gpa = gpa
    
    def prefix(self) :
        if self.gender == "Male" :
            return "Mr"
        elif self.gender == "Female" :
            return "Miss"

def main():
    students = [] 
    for _ in range(3) :
        students.append(Student(input(), input(), int(input()), input(), float(input())))

    id_finder = input()
    isHave = False
    for studentObj in students :
        if studentObj.id == id_finder :
            isHave = True
            print(f'{studentObj.prefix()} {studentObj.name} ({studentObj.age}) ID: {studentObj.id} GPA {studentObj.gpa:.2f}')

            break
    if not isHave :
        print("Student not found")
main()