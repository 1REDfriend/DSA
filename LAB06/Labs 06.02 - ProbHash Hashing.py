import json

class Student :
    std_id = int
    name = str
    gpa = float

    def __init__(self,std_id: int, name: str, gpa: float):
        self.std_id = std_id
        self.name = name
        self.gpa = gpa
    
    def get_std_id(self) :
        return self.std_id
    
    def get_name(self) :
        return self.name
    
    def get_gpa(self) :
        return self.gpa
    
    def print_details(self) :
        print(f'ID: {self.std_id}')
        print(f'Name: {self.name}')
        print(f'GPA: {self.gpa:.2f}')

class ProbHash :
    hash_table = list
    size = 0

    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * size

    def hash(self, key: int) :
        return self.hash_table

    
    def rehash(self, key: int) :
        temp = self.hash_table
        self.size = key
        self.hash_table.clear()

        self.hash_table = [None] * self.size

        for i in temp:
            index = i % self.size
            count = 0
            while self.hash_table[index] :
                count += 1
                self.hash_table[index + count]

            self.hash_table[index + count] = i
        return self.hash_table

    def insert_data(self, std: Student) :
        if len(list(filter(lambda x : x is not None, self.hash_table))) >= self.size :
            return print(f"The list is full. {std.get_std_id()} could not be inserted.")

        index = std.get_std_id() % self.size
        count = 0
        while self.hash_table[(index + count) % self.size] is not None:
            count += 1
        
        self.hash_table[(index + count) % self.size] = std
        print(f"Insert {std.get_std_id()} at index {(index + count) % self.size}")
    
    def search_data(self, std_id: int) -> Student:
        for i,student in enumerate(self.hash_table):
            if student is not None and student.get_std_id() == std_id :
                print(f"Found {std_id} at index {i}")
                return student
        print(f"{std_id} does not exist.")

class BinarySearch :
    data = []
    def __init__(self,data):
        self.insert_data(data)
    
    def insert_data(self, data) :
        try:
            parsed_data = json.loads(data)
        except json.JSONDecodeError:
            return

        for entry in parsed_data:
            if len(entry) >= 3:
                std_id = entry["id"]
                name = entry["name"]
                gpa = entry["gpa"]
                self.data.append(Student(std_id, name, gpa))

    def find(self, name) -> (Student, int):
        comparisons_t = 0
        left = 0
        right = len(self.data) - 1
        while left <= right:
            mid = (left + right) // 2
            comparisons_t += 1
            mid_student = self.data[mid]

            if mid_student.get_name() == name:
                print(f"Found {name} at index {mid}")
                return mid_student, comparisons_t
            elif mid_student.get_name() < name:
                left = mid + 1
            else:
                right = mid - 1

        print(f"{name} does not exists.")
        return None , comparisons_t

def main() :
    bn = BinarySearch(input())
    student, compareT = bn.find(input())
    if student :
        student.print_details()
    print(f"Comparisons times: {compareT}")
main()