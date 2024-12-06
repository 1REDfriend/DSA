"""Lab 01.01 - Is_Even"""
def main() :
    """main"""
    def is_even(num) :
        if num & 1 :
            return False
        return True

    print(is_even(int(input())))
main()