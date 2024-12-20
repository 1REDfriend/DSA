class Student :
    def __init__(self):
        self.data = list()
    
    def push(self, data) :
        self.data.append(data)

    def pop(self, data) :
        if self.data :
            self.data.pop()

def main() :
    students = list()
    student = Student

    m = int(input())
    n = int(input())
    