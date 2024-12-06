class Student :
    def __init__(self, name, gender, age, id, gpa) :
        self.name = name
        self.gender = gender
        self.age = age
        self.id = id
        self.gpa = gpa
    
    def generate_firstname(self, id_finder) :
        if self.id == id_finder :
            return self

def main():
    students = [] 
    students[0].find_by_id()