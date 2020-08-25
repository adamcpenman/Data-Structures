# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next  # The next node in the list


# class LinkedList:
#     def __init__(self):
#         self.head: Node = None  # points to the first node in the list
#         self.tail: Node = None  # Points to the last node in the list
#         self.length = 0

#     def __str__(self):
#         pass

#     def add_to_tail(self, value):
#         # Check if there's a tail
#         # If there is no tail (empty list)
#         if self.tail is None:
#             # Create a new node
#             new_tail = Node(value, None)
#         #    Set self.head and self.tail to the new node
#             self.head = new_tail
#             self.tail = new_tail
#         # If there is a tail (general case):
#         else:
#             # Create a new node with the value we want to add, next = None
#             new_tail = Node(value, None)
#             # Set current tail.next to the new node
#             old_tail = self.tail
#             old_tail.next = new_tail
#             # Set self.tail to the new node
#             self.tail = new_tail
#         self.length += 1

#     def remove_head(self):
#         # If not head (empty list)
#         if self.head is None:  # if self.head is None
#             return None
#         # List with one element:
#         if self.head == self.tail:
#             # Set self.head to current_head.next / None
#             current_head = self.head
#             self.head = None
#             # Set self.tail to None
#             self.tail = None
#             # Decrement length by 1
#             self.length = self.length - 1
#             return current_head.value
#         # If head (General case):
#         else:
#             # 	Set self.head to current_head.next
#             current_head = self.head
#             self.head = current_head.next
#             #  Return current_head.value
#             self.length = self.length - 1
#             return current_head.value

#     def remove_tail(self):
#         pass
#         # Remove Tail:
#         # Check if it's there
#         if self.tail is None:
#             return None
#         # General case:
#         # Start at head and iterate to the next-to-last node

#         # Stop when current_node.next == self.tail
#         # Save the current_tail value
#         # Set self.tail to current_node
#         # Set current_node.next to None
#         #
#         # List of 1 element:
#         # Save the current_tail.value
#         # Set self.tail to None
#         # Set self.head to None

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # 1. create the Node from the value
        new_node = Node(value)
        # So, what do we do if tail is None?
        # What's the rule we want to set to indicate that the linked
        # list is empty?
        # Would it be better to check the head?
        # Let's check them both: an empty linked list has an empty
        # head and an empty tail
        if self.head is None and self.tail is None:
            # in a one-element linked list, what should head and tail
            # be referring to?
            # have both head and tail referring to the single node
            self.head = new_node
            # set the new node to be the tail
            self.tail = new_node
        else:
            # These steps assume that the tail is already referring
            # to a Node
            # 2. set the old tail's next to refer to the new Node
            self.tail.set_next(new_node)
            # 3. reassign self.tail to refer to the new Node
            self.tail = new_node

    def remove_head(self):
        # if we have an empty linked list
        if self.head is None and self.tail is None:
            return
        # what if we only have a single elem in the linked list?
        # both head and tail are pointing at the same Node
        if not self.head.get_next():
            head = self.head
            # delete the linked list's head reference
            self.head = None
            # also delete the linked list's tail reference
            self.tail = None
            return head.get_value()
        val = self.head.get_value()
        # set self.head to the Node after the head
        self.head = self.head.get_next()
        return val

    def remove_tail(self):
        # if we have an empty linked list
        if self.head is None and self.tail is None:
            return

            # handle a single-element linked list
            if self.head is self.tail:
                value = self.head.get_value()
                self.head = None
                self.tail = None
                return value

        # if we have a non-empty linked list
        # we have to start at the head and move down the linked list
        # until we get to the node right before the tail
        # iterate over our linked list
        current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()
        # at this point, `current` is the node right before the tail
        # set the tail to be None
        val = self.tail.get_value()
        # move self.tail to the Node right before
        self.tail = current
        # remove new tail's reference to the old tail
        self.tail.next = None
        return val

    def contains(self, value):
        if not self.head:
            return False

        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def get_max(self):
        if not self.head:
            return None
        # reference to the largest value we've seen so far
        max_value = self.head.get_value()
        # reference to our current node as we traverse the list
        current = self.head.get_next()
        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.get_value() > max_value:
                # if so, update our max_value variable
                max_value = current.get_value()
            # update the current node to the next node in the list
            current = current.get_next()
        return max_value

# ll = Node(1)
# ll.set_next(Node(2))
# ll.next.set_next(Node(3))
# ll.next.next.set_next(Node(4))
# ll.next.next.next.set_next(Node(5))
