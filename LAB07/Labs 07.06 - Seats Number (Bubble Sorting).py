import json

data = json.loads(input())

def bubble_sort(data, last):
    comT = 0
    current = 0
    sorted = False

    while current <= last and not sorted :
        walker = last
        sorted = True
        while walker > current :
            comT += 1

            walker_str = "".join(filter(str.isalpha, data[walker]))
            walker_num = "".join(filter(str.isdigit, data[walker]))

            backward_str = "".join(filter(str.isalpha, data[walker - 1]))
            backward_num = "".join(filter(str.isdigit, data[walker - 1]))

            walker_num = int(walker_num) if walker_num else 0
            backward_num = int(backward_num) if backward_num else 0

            if walker_str < backward_str :
                sorted = False
                data[walker] , data[walker - 1] = data[walker - 1], data[walker]
            elif walker_str == backward_str and walker_num < backward_num :
                sorted = False
                data[walker] , data[walker - 1] = data[walker - 1], data[walker]
            walker -= 1

        print(data)
        current += 1
    print(f"Comparison times: {comT}")

bubble_sort(data, int(input()))
