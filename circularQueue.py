class CircularQueueArray:

    def __init__(self, size):

        self.size = size
        self.queue = [None] * size

        self.front = -1       # queue initially is empty. so no front and rear is available
        self.rear = -1

    # Check Full
    def is_full(self):

        return (self.rear + 1) % self.size == self.front

    # Check Empty
    def is_empty(self):

        return self.front == -1

    # Enqueue
    def enqueue(self, value):

        if self.is_full():
            print("Queue Overflow")
            return

        # First element
        if self.front == -1:    #if first element then both front and rear value start at index 0
            self.front = 0
            self.rear = 0

        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = value

        print(f"Inserted {value}")

    # Dequeue
    def dequeue(self):

        if self.is_empty():
            print("Queue Underflow")
            return None

        value = self.queue[self.front]

        # Only one element
        if self.front == self.rear:   #after last element dqueue(front==rear) , queue is empty. will get back to initial state.
            self.front = -1
            self.rear = -1

        else:
            self.front = (self.front + 1) % self.size

        print(f"Deleted {value}")

        return value

    # Display
    def display(self):

        if self.is_empty():
            print("Queue is Empty")
            return

        print("Queue:", end=" ")

        i = self.front

        while True:

            print(self.queue[i], end=" ")

            if i == self.rear:
                break

            i = (i + 1) % self.size

        print()


# Example
cq = CircularQueueArray(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)

cq.display()

cq.dequeue()
cq.dequeue()

cq.display()

cq.enqueue(50)
cq.enqueue(60)

cq.display()