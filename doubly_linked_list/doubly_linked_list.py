"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        # Create a new node
        new_node = ListNode(value)
        # If empty list:
        if self.head is None:
            # Set self.head = new_node
            self.head = new_node
        # Set self.tail = new_node
            self.tail = new_node
        # Else:
        else:
            # Set self.head.prev = new_node
            self.head.prev = new_node
        # Set new_node.next to self.head
            new_node.next = self.head
            # Set self.head = new_node
            self.head = new_node
            # New_node.previous = none
            # just to be explicit
            new_node.prev = None
        # increment
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        pass
        # General:
        # 	Old_head = self.head
        # 	Old_head.next = None
        # 	Self.head to self.head.next
        # 	Self.head.previous = None
        #   return old_head.value
        # One element:
        #   old_head = self.head
        # 	Self.head = None
        # 	Self.tail = None
        #   return old_head.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        # Create a new node
        new_node = ListNode(value)
        # If empty list:
        if self.tail is None:
            # Set self.head = new_node
            self.head = new_node
        # Set self.tail = new_node
            self.tail = new_node
        # Else:
        else:
            # Set self.head.prev = new_node
            self.tail.next = new_node
        # Set new_node.next to self.head
            new_node.prev = self.tail
            # Set self.head = new_node
            self.tail = new_node
            # New_node.previous = none
            # just to be explicit
            new_node.next = None
        # increment
        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        pass

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        # Check for empty pointers
        # Get previous node = node.prev
        previous_node = node.prev
        # Set prev_node.next to node.next
        if previous_node is None:
            # could just call self.remove_from_head()
            self.head = node.next
        else:
            previous_node.next = node.next
        # Next_node = node.next
        next_node = node.next
        # Set next_node.previous = previous_node
        if next_node is None:
            self.tail = node.prev
        else:
            next_node.prev = previous_node
        # Decrement length
        self.length -= 1
        # Set node.prev = None
        node.prev = None
        # Set node.next = None
        node.next = None
        # Return node.value
        return node.value

    """Returns the highest value currently in the list"""

    def get_max(self):
        # If length == 0 return None
        if self.length == 0:
            return None
        # If length == 1 return self.head.value
        if self.length == 1:
            return self.head.value
        # Current_max starts out as self.head.value
        current_max = self.head.value
        # Iterate through the list
        current_node = self.head
        # Stop when current_node is None
        while current_node is not None:
            # Compare current_max to each value and update current_max if value > current_max
            if current_max < current_node.value:
                current_max = current_node.value
        # Move current_node forward
            current_node = current_node.next
        # Return current_max
        return current_max
