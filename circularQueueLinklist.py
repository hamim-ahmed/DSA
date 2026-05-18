class Node:

    def __init__(self, data):

        self.data = data        #creating a new node to enque
        self.next = None


class CircularQueueLinkedList:

    def __init__(self):

        self.front = None                   #initial front and rear--->empty list
        self.rear = None

    # Check Empty
    def is_empty(self):

        if self.front is None:
            return True
        else:
            return False

    # Enqueue
    def enqueue(self, value):

        new_node = Node(value)

        # First node
        if self.is_empty():    #if empty first node....front and rear is the same.

            self.front = new_node
            self.rear = new_node

            self.rear.next = self.front         #rear pointing to the front----> making circular.

        else:

            self.rear.next = new_node

            self.rear = new_node

            self.rear.next = self.front         #rear pointing to the front----> making circular.

        print(f"Inserted {value}")

    # Dequeue
    def dequeue(self):

        if self.is_empty():

            print("Queue Underflow")
            return

        value = self.front.data

        # Single node
        if self.front == self.rear:    # if front == rear --> only one element left....deque will empty the queue.

            self.front = None
            self.rear = None

        else:

            self.front = self.front.next

            self.rear.next = self.front

        print(f"Deleted {value}")

        return value

    # Display
    def display(self):

        if self.is_empty():

            print("Queue is Empty")
            return

        print("Queue:", end=" ")

        temp = self.front

        while True:

            print(temp.data, end=" ")

            temp = temp.next

            if temp == self.front:
                break

        print()


# Example
cq = CircularQueueLinkedList()

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)

cq.display()

cq.dequeue()

cq.display()