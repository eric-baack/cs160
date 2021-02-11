"""Limited size max Binary Heap implementation"""
#!/usr/bin/env python3
# in this implementation, root of heap is node 0.  In each subtree, left node is odd,
# right node is even.  So, if at node j, parent node is (j-1) // 2.
# If at node k, left child is 2k +1, right child is 2k +2.
# Add notes here on perc up, perc down.
# Successfully implemented Apr 22, 2019.

class BinaryHeapMin:
    """Heap class implementation"""

    def __init__(self, limit: int = 0):
        self.heap = []
        self.size = 0
        self.max_size = limit
        self.smallest = None

    def perc_up(self, cur_idx):
        """Moving a node up"""
        while ((cur_idx // 2) - 1) > 0:
            if self.heap[cur_idx] > self.heap[cut_idx // 2 -1]:
                self.heapList[cur_idx // 2 -1] , self.heap[cur_idx] = self.heap[cur_idx], self.heapList[cur_idx // 2 -1]
            cur_idx = cur_idx // 2 - 1

   
    def perc_down(self, cur_idx):
        """Moving a node down"""
        while (cur_idx * 2 + 1) < self.size:   #check that left child exists
            min_child = self.get_min_child(cur_idx)
            if self.heap[cur_idx] > self.heap[min_child]:
                self.heap[cur_idx], self.heap[min_child] = self.heap[min_child], self.heap[cur_idx]
            cur_idx = min_child

    def insert(self, item):
        """Adding a new item"""
        self.heap.append(item)
        self.size = self.size + 1
        self.perc_up(self.size-1)

    def heapify(self, not_a_heap):
        """Turning a list into a heap"""
        self.heap = [] + not_a_heap[:]
        self.size = len(not_a_heap)
        cur_idx = self.size // 2 - 1
        while cur_idx >= 0:
            print(self)
            self.perc_down(cur_idx)
            cur_idx = cur_idx - 1
        print(self)

    def delMin(self):
        """ Removes smallest item from heap"""
        retval = self.heap[0]
        self.heap[0] = self.heap[(self.size - 1)]
        self.size = self.size - 1
        self.heap.pop()
        self.perc_down(0)
        return retval
    

    def get_min_child(self, parent_idx):
        """Getting a smaller child """
        mc = parent_idx * 2 + 1
        if parent_idx * 2 + 2 >= self.size:  # check if right child exists
            mc = parent_idx * 2 +1               # if not, return left child
        else:
            if self.heap[parent_idx * 2 + 1] < self.heap[parent_idx * 2 + 2]:
                mc = parent_idx * 2 + 1
            else:
                mc =  parent_idx * 2 + 2
        return mc

    def min_val(self):
        return self.heap[0]

    def __len__(self):
        """Get heap size"""
        return self.size

    def __str__(self):
        return str(self.heap)
        
def main():
    myHeap = BinaryHeapMin()
    #nlist = [60, 32, 46, 41, 45, 34, 50, 21, 10, 28]
    nlist = [6, 10, 7, 3, 1, 4, 9]
    myHeap.heapify(nlist)
    print(myHeap.min_val())
    myHeap.delMin()
    print(myHeap)

if __name__ == "__main__":
    main()
    
