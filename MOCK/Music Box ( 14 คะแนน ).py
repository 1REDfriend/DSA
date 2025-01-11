class Song :
    def __init__(self, name, genre, durations):
        self.name = name
        self.genre = genre
        self.durations = durations

    def show_info(self) :
        time = self.durations // 60
        time = str(time) + "." + f"{(self.durations % 60):02d}"
        return f"{self.name} <|> {self.genre} <|> {time}"
    
class Node :
    def __init__(self, data: Song):
        self.data = data
        self.next = None

class Queue :
    def __init__(self):
        self.head = None

    def enqueue(self, song: Song) :
        new_node = Node(song)
        current = self.head

        if not current :
            self.head = new_node
            return

        while current :
            current = current.next
        current = new_node

    def dequeue(self) :
        current = self.head
        if not current :
            print('Underflow! Dequeue from an empty queue')
            return None

        temp = self.head.data
        self.head = self.head.next
        return temp

    def peek(self) :
        current = self.head
        if not current :
            print('Underflow! peek from an empty queue')
            return None

        return self.head.data

    def isEmpty(self) :
        return self.head is None

    def show_Queue(self) :
        current = self.head
        count = 1

        if not current :
            print('Queue is empty!')
            return None

        while current :
            print("Queue#{count} {current.data.show_info()}")
            current = current.next
            count += 1

    def lastSong(self, time: int) :
        current = self.head
        count = 1
        if not current : 
            print('Nothing here! Please add some song')
            return None

        while current :
            time -= current.data.durations
            if time <= 0 :
                break
            current = current.next
            count += 1
        if time > 0 :
            self.lastSong(time)
        print("Queue#{count} {current.data.show_info()}")


    def removeSong(self, name: str) :
        current = self.head
        prev = None
        if not current :
            print(f"Can not Delete! {name} is not exist")
            return None

        while current :
            if current.data.name == name :
                new_node= Node(current.next)
                prev.next = new_node
                return None
            prev = current
            current = current.next
        
        print(f"Can not Delete! {name} is not exist")

    def groupSong(self) :
        current = self.head
        new_node = None
        q = Queue()
        while current :
            if current.data.genre == "JPOP" :
                if not new_node :
                    new_node = Node(current.data)
                else :
                    new_node = new_node.next
                    new_node = Node(current.data)
            current = current.next
        q.head = new_node
        current = q.head
        result = ''
        while current :
            result += current.data.name
            if current.next :
                result += " | "
            current = current.next
        print(f'JPOP: {result}')

        current = self.head
        new_node = None
        q = Queue()
        while current :
            if current.data.genre == "KPOP" :
                if not new_node :
                    new_node = Node(current.data)
                else :
                    new_node = new_node.next
                    new_node = Node(current.data)
            current = current.next
        q.head = new_node
        current = q.head
        result = ''
        while current :
            result += current.data.name
            if current.next :
                result += " | "
            current = current.next
        print(f'KPOP: {result}')

        current = self.head
        new_node = None
        q = Queue()
        while current :
            if current.data.genre == "R&B" :
                if not new_node :
                    new_node = Node(current.data)
                else :
                    new_node = new_node.next
                    new_node = Node(current.data)
            current = current.next
        q.head = new_node
        current = q.head
        result = ''
        while current :
            result += current.data.name
            if current.next :
                result += " | "
            current = current.next
        print(f'R&B: {result}')

    def undo(self) :
        pass

    def pop(self) :
        current = self.head
        if not current :
            return None

        while current.next :
            current = current.next
        temp = current
        current = None
        return temp

    def rev_queue(self) :
        q = Queue()
        current = self.head
        while current :
            q.enqueue(self.pop())

        self.head = q.head


def main():
    """this is main function"""
    q = Queue()
    while (choice := input()) != "End":
        command, data = choice.split(": ")
        match command:
            case "enqueue":
                q.enqueue(Song(*data.split("|")))
            case "dequeue":
                temp = q.dequeue()
                if temp:
                    temp.show_info()
            case "peek":
                temp= q.peek()
                if temp:
                    temp.show_info()
            case "isEmpty":
                print(q.isEmpty())
            case "showQueue":
                q.show_Queue()
            case "lastSong":
                q.lastSong(int(data))
            case "removeSong":
                q.removeSong(data)
            case "groupSong":
                q.groupSong()
            case "undo":
                q.undo()
            case "rev":
                q.rev_queue()
    q.show_Queue()
main()