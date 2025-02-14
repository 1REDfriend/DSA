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

            walker_str = "".join(filter(str.isalpha, data[walker]))
            walker_num = "".join(filter(str.isdigit, data[walker]))

            smallest_str = "".join(filter(str.isalpha, data[smallest]))
            smallest_num = "".join(filter(str.isdigit, data[smallest]))

            walker_num = int(walker_num) if walker_num else 0
            smallest_num = int(smallest_num) if smallest_num else 0

            if walker_str < smallest_str:
                smallest = walker
            elif walker_str == smallest_str and walker_num < smallest_num :
                smallest = walker
            walker += 1

        data[current], data[smallest] = data[smallest], data[current]
        print(data)

        current += 1

    print(f"Comparison times: {comT}")

selection_sort(data, int(input()))
