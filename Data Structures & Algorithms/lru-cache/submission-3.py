class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return self.cache[key].value
        else:
            return -1

    def add(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        self.cache[node.key] = node

    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        del self.cache[node.key]

    def put(self, key: int, value: int) -> None:
        newNode = Node(key, value)
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(newNode)

        elif len(self.cache) >= self.capacity:
            self.remove(self.head.next)
            self.add(newNode)

        else:

            self.add(newNode)

        
