class Item :
    name : str
    price : int
    weight : float

    def __init__(self, name: str, price: int, weight: float):
        self.name = name
        self.price = price
        self.weight = weight

    def get_name(self) -> str :
        return self.name

    def get_price(self) -> int :
        return self.price

    def get_weight(self) -> float :
        return self.weight

def knapsack(items: list[Item], k_cap: float):
    sorted_items = sorted(items, key=lambda x: (-x.get_price(), x.get_weight()))

    total_weight = 0
    total_price = 0

    print(f"Knapsack Size: {k_cap:.1f} kg")
    print("===============================")

    for item in sorted_items:
        if total_weight + item.get_weight() <= k_cap:
            total_weight += item.get_weight()
            total_price += item.get_price()
            print(f"{item.get_name()} -> {item.get_weight()} kg -> {item.get_price()} THB")

    print(f"Total: {total_price} THB")


def main():
    import json
    items = []
    num_items = int(input())
    while num_items != 0:
        item_in = json.loads(input())
        items.append(Item(item_in['name'], item_in['price'], item_in['weight']))
        num_items = num_items - 1
    knapsack_capacity = float(input())
    knapsack(items, knapsack_capacity)
main()