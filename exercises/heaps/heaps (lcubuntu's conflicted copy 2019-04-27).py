"""Limited size max Binary Heap implementation"""
#!/usr/bin/env python3

# Start with min heap implementation.  Modify max_child, perc_up, perc_down to deal with max root
# rather than min_root.
# Completed Apr 19, 2019.



class BinaryHeapMax:
    """Heap class implementation"""

    def __init__(self, limit: int = 10):
        self.heap = []
        self.size = 0
        self.max_size = limit
        self.smallest = None

    def perc_up(self, cur_idx):
        """Moving a node up"""
        while ((cur_idx + 1) // 2 - 1) >= 0:
            if self.heap[cur_idx] > self.heap[(cur_idx + 1) // 2 -1]:
                self.heap[(cur_idx + 1)  // 2 - 1] , self.heap[cur_idx] = self.heap[cur_idx], self.heap[(cur_idx + 1) // 2 - 1]
            cur_idx = (cur_idx + 1) // 2 - 1

    def perc_down(self, cur_idx):
        """Moving a node down"""
        while (cur_idx * 2 + 1) < self.size:   #check that left child exists
            max_child = self.get_max_child(cur_idx)
            if self.heap[cur_idx] < self.heap[max_child]:
                self.heap[cur_idx], self.heap[max_child] = self.heap[max_child], self.heap[cur_idx]
            cur_idx = max_child


    def insert(self, item):
        """Adding a new item"""
        if self.size == self.max_size:
            if self.smallest == None:
                self.smallest = item
            if item < self.smallest:
                print("Heap full:  item not added")
            else:
                smallest = self.heap[0]
                small_index = 0
                for heap_index in range(self.size):
                    if self.heap[heap_index] < smallest:
                        smallest = self.heap[heap_index]
                        small_index = heap_index
                self.heap[small_index] = item
                self.perc_up(small_index)
        else:    
            self.heap.append(item)
            self.size = self.size + 1
            self.perc_up(self.size - 1)

    def heapify(self, not_a_heap):
        """Turning a list into a heap"""
        self.heap = [] + not_a_heap[:]
        self.size = len(not_a_heap)
        self.smallest = min(not_a_heap)
        cur_idx = self.size // 2 - 1
        while cur_idx >= 0:
            #print(self)
            self.perc_down(cur_idx)
            cur_idx = cur_idx - 1
        print(self)

    def get_max_child(self, parent_idx):
        """Getting a larger child"""
        mc = parent_idx * 2 + 1
        if parent_idx * 2 + 2 >= self.size:  # check if right child exists
            mc = parent_idx * 2 +1               # if not, return left child
        else:
            if self.heap[parent_idx * 2 + 1] > self.heap[parent_idx * 2 + 2]:
                mc = parent_idx * 2 + 1
            else:
                mc =  parent_idx * 2 + 2
        return mc

    def __len__(self):
        """Get heap size"""
        return self.size

    def __str__(self):
        return str(self.heap)

    def max_val(self):
        return self.heap[0]

def main():
    myHeap = BinaryHeapMax(10)
    nlist = [60, 32, 46, 41, 45, 34, 50, 21, 10, 28]
    myHeap.heapify(nlist)
    myHeap.insert(5)
    print(myHeap)
    myHeap.insert(11)
    print(myHeap)
    print(myHeap.max_val())
    myHeap2 = BinaryHeapMax(5)
    myHeap2.insert("A")
    myHeap2.insert("Z")
    myHeap2.insert("C")
    myHeap2.insert("M")
    myHeap2.insert("V")
    print(myHeap2)
    b_movie_heap = BinaryHeapMax(5)
    b_movie_heap.insert("Alfred")
    b_movie_heap.insert("Batman")
    b_movie_heap.insert("Catwoman")
    b_movie_heap.insert("Dent")
    print(b_movie_heap)
    b_movie_heap.insert("Elfo")
    print(b_movie_heap)
    b_movie_heap.insert("Frodo")
    print(b_movie_heap)
    b_movie_heap.insert("Gordon")
    print(b_movie_heap)
    b_movie_heap.insert("Pavel")
    print(b_movie_heap)
    b_movie_heap.insert("Robin")
    print(b_movie_heap)

if __name__ == "__main__":
    main()

