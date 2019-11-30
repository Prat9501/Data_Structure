class node:
    """docstring for node."""

    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        """ adds new element in the last """
        new_node = node(data)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node

    def length(self):
        """ returns length of the linked list """
        curr =self.head
        count = 0
        while curr.next != None:
            count += 1
            curr = curr.next
        return count

    def show(self):
        """ displays the LL """
        curr = self.head
        elem = []
        while curr.next != None:
            curr = curr.next
            elem.append(curr.data)
        print(elem)

    def get_index_elem(self, index):
        """ returns the element at given index """
        if index >= self.length():
            print("Index out of range")
            return None
        curr_index = 0
        curr = self.head
        while True:
            curr = curr.next
            if curr_index == index:
                return curr.data
            curr_index += 1

    def delete_index_elem(self, index):
        """ deletes the element at given index """
        if index >= self.length():
            print("Index out of range")
            return
        curr_index = 0
        curr = self.head
        while True:
            prev = curr
            curr = curr.next
            if curr_index == index:
                prev.next = curr.next
                return
            curr_index += 1

my_list = linked_list()
my_list.append(2)
my_list.append(5)
my_list.append(7)
my_list.show()
print(my_list.get_index_elem(2))
my_list.delete_index_elem(1)
my_list.show()
