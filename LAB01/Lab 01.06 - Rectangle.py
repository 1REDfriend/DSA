class Rectangle:
  def __init__(self, height, width):
    self.height = height
    self.width = width

  def calculate_area(self):
    return self.height * self.width

  def calculate_perimeter(self):
    return self.height*2 + self.width*2

rec = Rectangle(float(input()),float(input()))
choice = input()

if choice == "area" :
    print(f"{rec.calculate_area():.2f}")
elif choice == "perimeter" :
    print(f"{rec.calculate_perimeter():.2f}")