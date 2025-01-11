class Song :
    def __init__(self, name, genre, durations):
        self.name = name
        self.genre = genre
        self.durations = int(durations) if isinstance(durations, str) else durations

    def show_info(self) :
        time = self.durations // 60
        time = str(time) + "." + f"{(self.durations % 60):02d}"
        return f"{self.name} <|> {self.genre} <|> {time}"

class Node :
    def __init__(self, data: Song):
        self.data = data
        self.next = None

class HistoryNode:
    def __init__(self, state_head):
        self.state_head = state_head  # เก็บสถานะหัวของ Queue
        self.next = None

class Queue :
    def __init__(self):
        self.head = None
        self.history_head = None

    def enqueue(self, song: Song) :
        self.save_state()  # บันทึกสถานะก่อนเพิ่มเพลง
        new_node = Node(song)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def dequeue(self) :
        if not self.head:
            print("Underflow! Dequeue from an empty queue")
            return None
        self.save_state()  # บันทึกสถานะก่อนลบเพลง
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
            print(f"Queue#{count} {current.data.show_info()}")
            current = current.next
            count += 1

    def lastSong(self, time: int) :
        current = self.head
        count = 1
        while current and time > 0:
            time -= current.data.durations
            if time <= 0:
                break
            current = current.next
            count += 1
        if not current:
            print('Nothing here! Please add some song')
        else:
            print(f"Queue#{count} {current.data.show_info()}")

    def removeSong(self, name: str):
        if not self.head:
            print(f"Can not Delete! {name} is not exist")
            return None
        self.save_state()  # บันทึกสถานะก่อนลบเพลง
        current = self.head
        prev = None
        while current:
            if current.data.name == name:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return
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
        if not self.history_head:
            print("No actions to undo!")
            return

        # โหลดสถานะก่อนหน้า
        previous_state_head = self.history_head.state_head
        self.history_head = self.history_head.next
        self.head = previous_state_head

    def save_state(self):
        if not self.head:
            new_history_node = HistoryNode(None)
        else:
            # Clone สถานะปัจจุบันของ Queue
            clone_head = Node(self.head.data)
            current_original = self.head.next
            current_clone = clone_head

            while current_original:
                current_clone.next = Node(current_original.data)
                current_clone = current_clone.next
                current_original = current_original.next

            new_history_node = HistoryNode(clone_head)

        # เชื่อมกับ History Linked List
        new_history_node.next = self.history_head
        self.history_head = new_history_node


    def pop(self) :
        if not self.head:
            return None
        if not self.head.next:
            temp = self.head
            self.head = None
            return temp
        current = self.head
        while current.next and current.next.next:
            current = current.next
        temp = current.next
        current.next = None
        return temp

    def rev_queue(self):
        q = Queue()
        while self.head:
            q.enqueue(self.pop().data)
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