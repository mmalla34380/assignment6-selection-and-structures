from array_matrix import CustomArray
from stack import Stack
from queue import Queue
from linked_list import SinglyLinkedList

if __name__ == "__main__":
    print("=== Stack ===")
    s = Stack()
    s.push(10)
    s.push(20)
    print("Top:", s.peek())
    s.pop()
    print("Top after pop:", s.peek())

    print("\n=== Queue ===")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print("Front:", q.peek())
    q.dequeue()
    print("Front after dequeue:", q.peek())

    print("\n=== Linked List ===")
    ll = SinglyLinkedList()
    ll.insert(100)
    ll.insert(200)
    ll.insert(300)
    print("List:", ll.traverse())
    ll.delete(200)
    print("After deletion:", ll.traverse())

    print("\n=== Array ===")
    arr = CustomArray()
    arr.insert(0, 5)
    arr.insert(1, 10)
    print("Access index 1:", arr.access(1))
    arr.delete(0)
    print("After delete index 0:", arr.data)
