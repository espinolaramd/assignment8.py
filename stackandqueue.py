#Diego Espinola
#03.24.2020
#assignment 8

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return repr(self.data)

class Linked_list:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        curr= self.head
        while curr:
            nodes.append(repr(curr))
            curr= curr.next
        return str(nodes)

    def add_head(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove_head(self):
        new_node = self.head
        self.head= self.head.next
        return new_node.data

class Stack:
    def __init__(self):
        self.mylist=Linked_list()

    def push(self,data):
        self.mylist.add_head(data)

    def pop(self):
        return self.mylist.remove_head()

class ListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return repr(self.data)


class LinkedListTail:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return str(nodes)

    def push(self, data):
        new_node = ListNode(data=data)
        if self.head is not None:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = self.head

    def pop_head(self):
        new_node = self.head
        self.head = new_node.next
        return new_node.data

    def pop_end(self):
        current_node = self.head
        previous_node = self.head
        while current_node.next:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = None
        return current_node.data

class Queue:
    def __init__(self):
        self.myqueue = LinkedListTail()

    def push(self,data):
        self.myqueue.push(data)

    def pop(self):
        return self.myqueue.pop_head()

