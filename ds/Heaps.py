"""
Min / Max Heaps and Min-max Heaps (three different kinds of heaps)

Min heap (parent node is lower in value than its childen nodes)
Max heap (parent node is higher in value than its childen nodes)
min-max heap (parent node is higher/lower than its children nodes depending on whether or not
    the parent node is in the min level or max level--which are alternating starting with 0 as min)

"""
import math

class heap:
    
    def __init__(self, heap_type="MIN"):
        self.array = list() # list representation of a complete binary tree
        self.mode = heap_type

    def get_right_child(self, index):
        """ Returns the right child of a given index position"""
        return 2 * index + 2

    def get_left_child(self, index):
        """ Returns the left child of a given index position"""
        return 2 * index + 1

    def get_parent(self, index):
        return math.floor(index - 1 / 2)

    def heapify(self, index):
        """
        Rearranges the heap elements to maintain the heap properties
        O(n)
        """
        largest_index = index
        l_index = self.get_left_child(index)
        r_index = self.get_right_child(index)

        if l_index < len(self.array) and
            self.array[l_index] > self.array[index]:
            largest_index = l_index

        if r_index < len(self.array) and
            self.array[r_index] > self.array[index]:
            largest_index = r_index

        if largest_index != index:
            self.swap(index, largest_index)
            heapify(largest_index)

    def insert(self, value):
        """
        Insert key into heap without violating heap properies
        """
        if len(self.array):
            self.array.append(value)
            current_index = len(self.array) - 1
            parent_index = self.get_parent(current_index)
            while (current_index != 0 and
                   self.array[parent_index] < self.array[current_index]):
                   self.swap(parent_index, current_index)
                   current_index = parent_index
                   parent_index = self.get_parent(current_index)
        else:
            self.array.append(value) # first entry

    def swap(self, index_1, index_2):
        """
        Swap two indexes together
        """
        temp = self.array[index_1]
        self.array[index_1] = self.array[index_2]
        self.array[index_2] = temp

    def delete(self, value):
        """
        delete key into heap without violating heap properies
        """
        pass

    def extract(self, value):
        """
        Same as delete but returns the value
        """
        pass

    def isEmpty(self):
        """
        boolean if array for the heap is empty or not
        """
        return bool(self.array)
    
    def getRoot(self):
        """
        Returns the min or max depending on the type of heap we have
        """
        return self.array[0]

    def print_heap(self):
        print(self.array)

if __name__ == "__main__":
    h = heap()
    h.insert(10)
    h.insert(12)
    h.insert(1)
    h.print_heap()
