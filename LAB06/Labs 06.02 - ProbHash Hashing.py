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
            return print(f"The list is full. {std.get_std_id()} cloud not be inserted.")
        
        index = std.get_std_id() % self.size
        count = 0
        while self.hash_table[(index + count) % self.size] is not None:
            count += 1
        
        self.hash_table[(index + count) % self.size] = std
        print(f"Insert {std.get_std_id()} at index {(index + count) % self.size}")
    
    def search_data(self, std_id: int) :
        for i,student in enumerate(self.hash_table):
            if student is not None and student.get_std_id() == std_id :
                print(f"Found {std_id} at index {i}")
                return student
        print(f"{std_id} doese not exist.")

def main():
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")
main()