import json

def seat_insert_sort(data, last) :
    comT = 0
    for current in  range(1, last+1) :
        result = data[current]
        walker = current - 1

        while walker >= 0:
            comT += 1
            walker_str = "".join(filter(str.isalpha, data[walker]))
            walker_num = "".join(filter(str.isdigit, data[walker]))

            result_str = "".join(filter(str.isalpha, result))
            result_num = "".join(filter(str.isdigit, result))

            walker_num = int(walker_num) if walker_num else 0
            result_num = int(result_num) if result_num else 0

            if walker_str > result_str:
                data[walker + 1] = data[walker]
                walker -= 1
            elif walker_str == result_str and walker_num > result_num:
                data[walker + 1] = data[walker]
                walker -= 1
            else:
                break
        data[walker + 1] = result
        print(data)
    print(f"Comparison times: {comT}")

seat_insert_sort(json.loads(input()), int(input()))