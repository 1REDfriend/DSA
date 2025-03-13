import json

def knapsackV2(goods, total_capacity):
    item_count = len(goods)

    dp_table = [
        [0 for _ in range(total_capacity + 1)] for _ in range(item_count + 1)
    ]

    for idx in range(1, item_count + 1):
        for curr_weight in range(total_capacity + 1):
            item_name, value, mass = goods[idx - 1]
            if mass <= curr_weight:
                dp_table[idx][curr_weight] = max(dp_table[idx - 1][curr_weight],
                                               dp_table[idx - 1][curr_weight - mass] + value)
            else:
                dp_table[idx][curr_weight] = dp_table[idx - 1][curr_weight]

    chosen_items = []
    remaining_weight = total_capacity
    max_value = dp_table[item_count][total_capacity]

    for idx in range(item_count, 0, -1):
        if dp_table[idx][remaining_weight] != dp_table[idx - 1][remaining_weight]:
            item_name, value, mass = goods[idx - 1]
            chosen_items.append((item_name, mass, value))
            remaining_weight -= mass

    chosen_items.sort(key=lambda x: x[0])

    return max_value, chosen_items

def main() :
    max_value, chosen_items = knapsackV2(
        json.loads(input().strip()),
        int(input().strip())
    )

    print(f"Total: {max_value}")
    for item_name, mass, value in chosen_items:
        print(f"{item_name} -> {mass} kg -> {value} THB")

main()