"""
[2022 / 02 / 04] Linked Lists

Operations to implement:
    Access [!done]
    Search
    Insert (tail-end) [!done]
    Insert (head-end) [!done]
    Remove (from certain position)
    Remove (from head) [!done] 
    Remove (from tail) [!done]
"""


class Node: 
    
    def __init__(self, data=None):
        self.next = None
        self.data = data

class LinkedList:
    
    def __init__(self):
        self.head = None

    def add_node_end(self, value):
        """
        Add new nodes to the end of the ll
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        else:
            iterator = self.head
            while iterator.next is not None:
                iterator = iterator.next
            iterator.next = new_node

    def add_node_head(self, value):
        """
        Add a new node to the head of the ll
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def delete_node_end(self):
        if self.head is None:
            return # empty linkedlist

        if self.head.next is None: # head is the only thing missing 
            self.head = None
            return

        iterator = self.head
        while iterator.next.next is not None:
            iterator = iterator.next
        iterator.next = None

    def delete_node_head(self):
        """
        Add a new node to the head of the ll
        """
        if self.head is None:
            return
        else:
            self.head = self.head.next

    def display_nodes(self):
        """
        Display the nodes within the LinkedList
        """
        print("Display --- " )
        iterator = self.head
        while iterator is not None:
            print(iterator.data)
            iterator = iterator.next

    def search_for_val(self, value):
        position = 0
        iterator = self.head
        while iterator is not None:
            if iterator.data == value:
                print(f"{iterator.data} @ node #{position}")
            position += 1
            iterator = iterator.next

if __name__ == "__main__":
    ll = LinkedList()
    ll.add_node_end(1)
    ll.add_node_end(2)
    ll.add_node_end(3)
    ll.display_nodes()
    ll.search_for_val(2)
