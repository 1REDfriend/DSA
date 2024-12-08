import random
class แล้วแต่แอพ :
    def __init__(self, foodlist):
        self.foodlist = foodlist
    
    def random_foods(self) :
        return self.foodlist[random.random(len(self.foodlist))]
    
    def list_foods(self) :
        self.foodlist.sort()
        print(self.foodlist)

if __name__ == "__main__" :
    app = แล้วแต่แอพ(["Pizza", "Fried Chicken", "Hamburger", "Steak"])
    app.list_foods()