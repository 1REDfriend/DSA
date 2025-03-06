class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

def knapsack(amount, itemList):
    itemList.sort(key=lambda x: x.price / x.weight, reverse=True)

    backpack_size = amount
    total_value = 0
    selected_items = []

    for item in itemList:
        if amount >= item.weight:
            selected_items.append(item)
            total_value += item.price
            amount -= item.weight

    print(f"Knapsack Size: {backpack_size:.1f} kg")
    print("===============================")
    for item in selected_items:
        print(f"{item.name} -> {item.weight} kg -> {item.price} THB")
    print(f"Total: {total_value} THB")

def main():
    import json
    items = []
    num_items = int(input())
    while num_items != 0:
        item_in = json.loads(input())
        items.append(Item(item_in['name'], item_in['price'], item_in['weight']))
        num_items -= 1
    knapsack_capacity = float(input())
    knapsack(knapsack_capacity, items)

if __name__ == "__main__":
    main()