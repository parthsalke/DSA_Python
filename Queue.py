from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

q=Queue()
q.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
q.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
q.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})

print(q.size())
print(q.is_empty())
print(q.dequeue())
print(q.size())
print("***********************************************************")
#Queue excerise for food ordering at resturant
import time
import threading

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

queue=Queue()
def placeorder(orders):
    for order in orders:
        print("Placing order for:", order)
        queue.enqueue(order)
        time.sleep(0.5)
def serveorder():
    time.sleep(1)
    while True:
        order=queue.dequeue()
        print("Serving order for:",order)
        time.sleep(2)
if __name__ == '__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=placeorder, args=(orders,))
    t2 = threading.Thread(target=serveorder)

    t1.start()
    t2.start()