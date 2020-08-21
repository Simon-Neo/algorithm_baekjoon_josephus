




class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Circular_linklist():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def append(self, data):

        if self.is_empty():
            self.head = Node(data)
            self.tail = self.head
        else:
            # Add New node to tail
            self.tail.next = Node(data)
            # update tail node
            self.tail = self.tail.next
            # connect tail -> head
            self.tail.next = self.head

        self.size += 1



    def pop(self, before_node):

        target_node = before_node.next
        before_node.next = target_node.next

        if target_node == self.head:
            self.head = target_node.next
        elif target_node == self.tail:
            self.tail = target_node.next

        self.size -= 1
        if self.is_empty():
            self.head = None
            self.tail = None


        return target_node.data

    def render(self):
        index_node = self.head

        result_str = '<'
        while(True):
            result_str += str(index_node.data) + ', '
            if index_node == self.tail:
                break

            index_node = index_node.next

        result_str = result_str.rstrip(', ')
        print(result_str + '>')

linkedlist = Circular_linklist()
n = 7
k = 3

for i in range(1, n + 1):
    linkedlist.append(i)

linkedlist.render()

result_str = '<'

before_node = linkedlist.tail


while not linkedlist.is_empty():
    for _ in range(k - 1):
        before_node = before_node.next

    result_str += str(linkedlist.pop(before_node)) + ', '

result_str = result_str.rstrip(', ')

print(result_str + '>')










