class Elevator:
  def __init__(self, max_floor):
    self.current_floor = 1
    self.max_floor = max_floor

  def go_to_floor(self, floor=int):
    if floor > self.max_floor :
        print("Invalid Floor!")
    else :
        self.current_floor = floor

  def report_current_floor(self):
    print(self.current_floor)

if __name__ == "__main__" :
    myElevator = Elevator(int(input()))
    while True :
      myFloor = input()
      if myFloor != "Done" :
        myElevator.go_to_floor(int(myFloor))
      else :
        break
    myElevator.report_current_floor()
    