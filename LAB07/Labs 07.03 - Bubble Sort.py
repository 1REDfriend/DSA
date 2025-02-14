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
            if data[walker] < data[walker-1] :
                sorted = False
                data[walker] , data[walker - 1] = data[walker - 1], data[walker]
            walker -= 1

        print(data)
        current += 1
    print(f"Comparison times: {comT}")

bubble_sort(data, int(input()))
