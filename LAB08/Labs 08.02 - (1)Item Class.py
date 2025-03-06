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


def main():
    import json
    item_in = json.loads(input())
    item = Item(item_in["name"], item_in["price"], item_in["weight"])
    print(item.get_name(), item.get_price(), item.get_weight(), sep='\n')

main()