"""This is the module level docstring."""

# import typing

class _SNode(item = None, next_node = None):
    """Private class for single linking nodes."""
    def __init__(self):
        item = self.item
        next_node = self.next_node

class SLinkedList(_SNode):
    """Implements the Singly Linked List ADT using an array.\n
    Specification (Complexity given as (Space, Time)):
    SLinkedList() - Creates an instance StackArr instance (stack implemented with a list).
    add(item) - Pushes an item on the top of the stack: Complexity: (O(1), O(1)).
    remove(item) - Removes and returns the item on the top of the stack: Complexity: (O(1), O(n)).
    search(item) - Returns the item on the top of the stack: Complexity: (O(1), O(n)).
    is_empty() - Returns True of the stack is empty and False otherwise. Complexity: (O(1), O(1)).
    size() - Returns the number of items in the stack."""

    def __init__(self, item = None):
        """Initialize a singly linked list."""
        self.head = _SNode(item, None)

    def add(self, item):
        """Adds an item to the head of the list."""
        new_node = SNode(item, self.head)
        self.head = new_node

    def remove(self, item):
        """Searches for the specified item in the list. If found the item is removed and returned. Otherwise, None is returned."""
        current_node = self.head
        if current_node.item == item:
            pop(current_node)
        while current_node != None:
            if current_node.next_node == item:
                current_node.next_node = current_node.next_node.next_node
                return True
            else:
                current_node = current_node.next_node
        return False

    def search(self, item):
        """Searches for the specified item in the list and returns True if item is in 
        the list and False otherwise."""
        current_node = self.head
        while current_node != None:
            if current_node.next_node == item:
                current_node.next_node = current_node.next_node.next_node
                return True
            else:
                current_node = current_node.next_node
        return False

    def is_empty(self):
        """Returns a True if the list is empty and False otherwise."""
        return self.head.item == None and self.head.next_node == None

    def size(self):
        """Returns the number of nodes in the linked list"""
        current_node = self.head
        size = 0
        while current_node != None:
            size += 1
            current_node = current_node.next_node
        return size

    def append(item):
        """"""
        pass
 
    def index(item):
        """"""
        pass

    def insert(self, item, position):
        """Inserts a new item at the specified position in the list. Returns True 
        if position < list size and False otherwise."""
        current_node = self.head
        current_pos = 0
        while current_node != None:
            if current_pos == position:
                if current_position.next_node != None:
#                     new_node = _SNode(item, current_position.next_node)
#                     current_position.next_node = new_node
                    current_position.next_node = _SNode(item, current_position.next_node)
                    return True
                else:
                    current_position.next_node = _SNode(item, None)
                    return True
            current_pos += 1
            current_node = current_node.next_node
        return False
        
    
    def pop(self):
        """Removes and returns the head of the list, and returns None if the list is empty."""
        old_head = self.head
        self.head = self.head.next_node
        return old_head
    
    def pop(self, position):
        """Removes and returns an item at the specified position within the list."""
        current_node = self.head
        current_pos = 0
        while current_node != None:
            if current_pos == position:
                if current_position.next_node != None:
                    current_position.next_node = _SNode(item, current_position.next_node)
                    return True
                else:
                    current_position.next_node = _SNode(item, None)
                    return True
            current_pos += 1
            current_node = current_node.next_node
        return False

class _DNode(item = None, next_node = None, previos_node = None):
    """Private class for single linking nodes."""
    def __init__(self):
        item = self.item
        next_node = self.next_node
        previous_node = self.previous_node

class DLinkedList(_DNode):
        """Implements the Singly Linked List ADT using an array.\n
    Specification (Complexity given as (Space, Time)):
    SLinkedList() - Creates an instance StackArr instance (stack implemented with a list).
    add(item) - Pushes an item on the top of the stack: Complexity: (O(1), O(1)).
    remove(item) - Removes and returns the item on the top of the stack: Complexity: (O(1), O(n)).
    search(item) - Returns the item on the top of the stack: Complexity: (O(1), O(n)).
    is_empty() - Returns True of the stack is empty and False otherwise. Complexity: (O(1), O(1)).
    size() - Returns the number of items in the stack.
    append()
    index(item)
    insert(item)
    pop
    pop(pos)"""
    
    def __init__(self, item = None):
        self.head = _DNode(item, None, None)
        self.tail = self.head
    
    def add(self, item):
        """"""
        after_head = self.head.next_node
        self.head = _DNode(item, after_head, None)
        after_head.previous = self.head

    def remove(self, item):
        """"""
        pass

    def search(self, item):
        """"""
        pass

    def is_empty(self, item):
        """"""
        return not self.head

    def size(self):
        """"""
        pass

    def append(self, item):
        """"""
        pass

    def index(self, item):
        """"""
        pass

    def insert(self, item, position):
        """"""
        pass

    def pop(self):
        """"""
        self.head = self.head.next_node
        self.head.previous = None

    def pop(self, position):
        """"""
        pass

class StackArr:
    """Implements the stack ADT using an array.\n
    Specification:\n
    StackArr() - Creates an instance StackArr instance (stack implemented with a list).\n
    push(item) - Pushes an item on the top of the stack.\n
    pop() - Removes and returns the item on the top of the stack.\n
    peek() - Returns the item on the top of the stack.\n
    is_empty() - Returns True of the stack is empty and False otherwise.\n
    size() - Returns the number of items in the stack.\n"""

    def __init__(self, stack_arr = None):
        """Initialize the stack with an array or the default argument of None."""
        self._items = stack_arr

    def push(self, item):
        """Pushes an item on the top of the stack."""
        self._items.append(item)

    def pop(self):
        """Removes and returns the item on the top of the stack."""
        item = self._items[-1]
        self._items = self._items[:-1]
        return item

    def peek(self):
        """Returns the item on the top of the stack."""
        return None if (len(self._items) == 0 or self._items == None) else self._items[-1]

    def is_empty(self):
        """Returns True of the stack is empty and False otherwise."""
        return not self._items

    def size(self):
        """Returns the number of items in the stack."""
        return 0 if self.items == None else len(self._items)

# class StackLL:
#     pass

class Queue:
    """Implements the Queue ADT using an array.\n
    Specification:\n
    Queue() - Creates an instance StackArr instance (queue implemented with a list).\n
    enqueue(item) - Pushes an item on the top of the queue.\n
    dequeue() - Removes and returns the item on the top of the queue.\n
    is_empty() - Returns True of the queue is empty and False otherwise.\n
    size() - Returns the number of items in the queue.\n"""
    
    def __init__(self):
        """"""
        self._items = []

    def enqueue(self, item):
        """"""
        self.items.push(item)
    
    def dequeue(self, item):
        """"""
        self.items.pop()
    
    def is_empty(self, item):
        """"""
        return not self.items
    
    def size(self, item):
        """"""
        return len(self.items)

# class SLQueue:
#     pass

# class DLQueue:
#     pass

# class Dequeue:
#     pass
