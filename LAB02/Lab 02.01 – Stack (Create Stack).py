class ArrayStack :
    def __init__(self):
        self.size = 0
        self.data = list()

    def push(self, input_data):
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1
    
    def pop(self) :
        if self.data :
            self.data.pop()
            self.size -= 1
        else :
            print( "Underflow: Cannot pop data from an empty list")
            return None

    def is_empty(self):
        if self.data or self.size:
            return False
        return True
    
    def get_stack_top(self) :
        if self.data :
            temp = self.data.copy()
            needData = temp.pop()
            return needData
        else :
            print("Underflow: Cannot get stack top from an empty list")
            return None
    
    def get_size(self) :
        return int(self.size)
    
    def print_stack(self) :
        temp = self.data
        print(temp)

def main():
    stack = ArrayStack()
    text_in = input()
    while text_in.lower() != "exit":
        condition, data = text_in.split(": ")
        if condition == "Push":
            stack.push(data)
        elif condition == "Pop":
            stack.pop()
        elif condition == "Top":
            print(stack.get_stack_top())
        elif condition == "Size":
            print(stack.get_size())
        elif condition == "Empty":
            print(stack.is_empty())
        elif condition == "Print":
            stack.print_stack()
        else:
            print("Invalid Condition!")
        text_in = input()
    stack.print_stack()

main()