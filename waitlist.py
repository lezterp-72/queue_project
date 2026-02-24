import random

class Student:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.sid = random.randint(1000, 9999)

    def __str__(self):
        return f"{self.first} {self.last} ID: {self.sid}"


class Node:
    def __init__(self, Student):
        self.data = Student
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        return_str = "Waitlist Status: "
        node = self.head
        if not node:
            return_str = return_str + "Empty"
            return return_str
        while node:
            if node.next:
                return_str = return_str + node.data.first + " " + node.data.last + " -- "
            else:
                return_str = return_str + node.data.first + " " + node.data.last
            node = node.next
        return_str = return_str + f"\nSize is: {self.size}"
        return return_str


    def pop_left(self):
        if not self.head:
            return None
        current_head = self.head
        self.head = self.head.next
    
        self.size -= 1
        print(f"{current_head.data} has been moved off the waitlist.")


    def add(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node

        else:
            current = self.head
            while current.next:
                if not current.next:
                    break
                current = current.next
            current.next = new_node
        
        self.size += 1

    def empty(self):
        if self.head: return False
        return True



# Creates a main function(?) similar to Java
if __name__ == '__main__' :
    s1 = Student('Amy', 'Mathers')
    print(s1)
    s2 = Student('Beth', 'Chambers')
    print(s2)
    s3 = Student('Carlos', 'Ruiz')
    print(s3)
    print("\n")

    waitlist = Queue()
    waitlist.add(s1)
    waitlist.add(s2)
    waitlist.add(s3)
    
    print(waitlist)
    print("\n")
    waitlist.pop_left()
    print(waitlist)
    print("\n")
    waitlist.pop_left()
    print(waitlist)
    print("\n")
    waitlist.pop_left()
    print(waitlist)


