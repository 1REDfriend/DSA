student = []
for _ in range(3) :
    student.append([input(),input(),int(input()),input(),float(input())])

find = input()
isFound = False
for i in student :
    if i[3] == find :
        isFound = True
        if i[1] == "Male" :
            print(f"Mr {i[0]} ({i[2]}) ID: {i[3]} GPA {float(i[4]):.2f}")
        elif i[1] == "Female" :
            print(f"Miss {i[0]} ({i[2]}) ID: {i[3]} GPA {float(i[4]):.2f}")

if not isFound :
    print("Student not found")