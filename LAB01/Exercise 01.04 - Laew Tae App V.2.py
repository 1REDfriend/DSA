import random
class แล้วแต่แอพ :
    def __init__(self, foodlist=list):
        self.foodlist = foodlist
    
    def random_foods(self) :
        return self.foodlist[random.random(len(self.foodlist))]
    
    def list_foods(self) :
        self.foodlist.sort()
        print(self.foodlist)

    def add_food_items(self,name) :
        self.foodlist.append(name)

if __name__ == "__main__" :
    app = แล้วแต่แอพ(["Pizza", "Fried Chicken", "Hamburger", "Steak"])
    
    for _ in range(int(input())) :
        app.add_food_items(input())
    
    app.list_foods()