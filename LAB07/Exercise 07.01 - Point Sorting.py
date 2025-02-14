import json

data = json.loads(input())

def selection_sort(data , last):
    comT = 0
    current = 0

    while current < last:
        smallest = current
        walker = current + 1

        while walker <= last:
            comT += 1
            if sum(data[walker]) < sum(data[smallest]):
                smallest = walker
            walker += 1

        data[current], data[smallest] = data[smallest], data[current]
        current += 1

    return data


