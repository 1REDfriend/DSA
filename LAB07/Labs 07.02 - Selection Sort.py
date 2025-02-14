import json

data = json.loads(input())

def selection_sort(data, last):
    comT = 0
    current = 0

    while current < last:
        smallest = current
        walker = current + 1

        while walker <= last:
            comT += 1
            if data[walker] < data[smallest]:
                smallest = walker
            walker += 1

        data[current], data[smallest] = data[smallest], data[current]
        print(data)

        current += 1

    print(f"Comparison times: {comT}")

selection_sort(data, int(input()))
