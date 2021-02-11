# Nodes by themselves not very useful - need linked list to keep track of nodes.

class Node:
    def __init__(self, init_value):
        self._value = init_value
        self._next = None
    
    def get_data(self):
        return self._value

    def set_data(self, new_data):
        self._value = new_data
    
    data = property(get_data, set_data)
    
    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, new_next):
        self._next = new_next

    def __str__(self):
        return str(self._value)

# This list is unordered.  
class LinkedList:
    def __init__(self):
        self._head = None
        # self._tail = None
        self._size = 0
    
    def __len__(self) -> int:
        return self._size
    
    # There are multiple ways to implemnt the list.  
    # Could build list from nodes, then join
    # Both OK - internal
    def __str__(self):
        list_str = '['
        current = self._head

        while current:
            list_str += str(current)
            if current.next:
                list_str += ', '
            current = current.next
        list_str += ']'
        return list_str
    
# alternative implementation of str
    def __stralt__(self):
        my_list = []
        current = self._head

        while current:
            my_lilst.append(current, @staticmethod
            current = current.next
        return my_list_str = f"[{', '.join(my)list)}]" 

    # something to avoid
    # if self._head is None:
        #return True
    # else:
        # return false
    #Better - see next line.  One line does the job of four.

    def is_empty(self) -> bool:
        return self._head is None  # See above for bad version
    
    def size(self) -> int:
        return self._size
        # alternative:  return self.__len__()
        # advantage:  will allow change to just one method - len
    # This is better than below - which repeats code      
    def add(self, new_node: object) -> None:
        new_node.next = self._head
        self._head = new_node
        self._size += 1

    ## Alternative.  Note duplication of code - not needed!
    ## def add(self, new_node: object) -> None:
        # if self.head is None: # empty list
        #     self._head.next  new nodes
        #     self._size +=1
        # else:
        #     new_node.next = self._head
        #     self._head = new_node
        #     self._size +=1

# Do not shift head.  Keep it pointing to 1st element.
# Instead use another variable - current - to track nodes
# Note:  head is NOT a node, it points to first node
    def search(self, value) -> bool:
        current = self._head
        while current:   # if current = none, current = false.
            if current.data == value:
                return True
            current = current.next
        return False

    def index(self, value) -> int:
        idx = 0
        current = self._head
        while current:
            if current.data == value:
                return idx
            current = current.next
            idx += 1
        return -1  # Convention:  if not found, return -1
    # This is a bit tricky.  There are some options to consider.
    # Generally, don't move the head!
    # Changed:  have specified that append takes object, returns None
    # Add doc strings - aim at same level of experience
    def append(self, new_node: object) -> None:  # add node, or add value?  a_list.add(Node(5))
        """ 
        Append a new node to the list at end
        
        takes Node object as parameter

        raises ValueError if boject is not a node
        """
        if not self._head:  # list is empty   or:  a_list.add(5).  Where does
            self._head = new_node       # the new node get created?  in append?
            self._size += 1             # or in main?  In this program, main
            return                      # adds the nodes.
        current = self._head  #otherwise
        while current.next: # move to end of next (until current.next = None)
            current = current.next 
        current.next = new_node
        self._size += 1

    def insert(self, pos: int, new_node: object) -> None:
        """
        insert new node (not value - node!) in a given position

        takes position (int) and new node (object)

        return None
        """
        current = self._head
        idx = 0
        if pos <= 0:
            self.add(new_node)  # automatically changes size
            return
        if pos > self._size:
            self.append(new_node) # automatically changes size
            return
        while idx < pos - 1:  # current will not be None in this range - no need to check
            idx += 1
            current = current.next

        new_node.next = current.next  # get to prior position, get next, move it to new node
        current.next = new_node # link prior to new node
        self._size += 1

    # most complex - need to check for several exceptions.
    def pop(self, idx = None):  # can be called without index - defaults to None.  (but can be passed idx)
        if not self._head:
            raise Exception('Cannot pop from an empty list')  # could make a custom exception, if defined
        if idx == None:
            idx = self._size
        if idx < 0:  # option - this could be implemented
            raise ValueError('Negative')
        current = self._head
        prev = None
        cur_idx = 0
        while current.next and cur_idx < idx:
            prev = current
            current = current.next
            cur_idx += 1
        result = current.data
        if prev:            # Without pointer to node, node will be removed by garbage collector
            prev.next = current.next
        else:
            self._head = current.next
        self._size -= 1
        return result

def main():
    # print('Working with nodes')
    # n = Node('A')
    # print(n.data)
    # print(n.next)
    # print(n)

    # m = Node('B')
    # n.next = m
    # print(n.next)

    print('Working with lists')
    ll = LinkedList()
    print(ll.size())  # 0
    # print(type(ll))  # LinkedList
    # print('Printing a list')
    # print(ll)
    # ll.add(Node('Q'))
    # print(ll)  # [Q]
    # ll.add(Node('A'))
    # print(ll)  # [A, Q]
    # ll.add(Node('D'))
    # print(ll)  # [D, A, Q]
    # print(len(ll))
    # print(ll.search('Z'))
    # print(ll)  # [D, A, Q]
    # print(len(ll))
    # print(ll.index('D'))  # 0
    # print(ll)  # [D, A, Q]
    # print(len(ll))
    # print(ll.index('Z'))  # -1
    # print(ll)  # [D, A, Q]
    # print(len(ll))
    # print('Inserting a new node')
    # ll.insert(0, Node('K'))
    # print(ll)  # [K, D, A, Q]
    # print(len(ll))  # 4
    # ll.insert(2, Node('M'))
    # print(ll)  # [K, D, M, A, Q]
    # print(len(ll))  # 5
    print(ll)  # []
    ll.append(Node('R'))
    ll.append(Node('Q'))
    ll.append(Node('T'))
    ll.append(Node('S'))
    print(ll)  # [R, Q, T, S]
    print(len(ll))  # 4
    print(ll.pop(1))  # Q
    print(ll)  # [R, T, S]
    print(len(ll))  # 3
    print(ll.pop())  # S
    print(ll)  # [R, T]
    print(len(ll))  # 2
    print('---')
    print(ll.pop(0))  # R
    print(ll)  # [T]
    print(len(ll))  # 1

if __name__ == '__main__':
    main()