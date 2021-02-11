"""Limited size max Binary Heap implementation"""
#!/usr/bin/env python3

# Start with min heap implementation.  Modify max_child, perc_up, perc_down to deal with max root
# rather than min_root


class BinaryHeapMax:
    """Heap class implementation"""

    def __init__(self, limit: int = 0):
        self.heap = []
        self.size = 0
        self.max_size = limit
        self.smallest = None

    def perc_up(self, cur_idx):
        """Moving a node up"""
        while cur_idx // 2 - 1 > 0:
            if self.heap[cur_idx] > self.heap[cut_idx // 2 -1]:
                self.heapList[i // 2 -1] , self.heap[cur_idx] = self.heap[cur_idx], self.heapList[i // 2 -1]
            cur_idx = cur_idx // 2 - 1

    def perc_down(self, cur_idx):
        """Moving a node down"""

        raise NotImplementedError

    def insert(self, item):
        """Adding a new item"""
        raise NotImplementedError

    def heapify(self, not_a_heap):
        """Turning a list into a heap"""
        self.heap = [] + not_a_heap[:]
        self.size = len(not_a_heap)
        cur_idx = self.size // 2 - 1
        while cur_idx >= 0:
            self.perc_down(cur_idx)
            cur_idx = cur_idx - 1

    def get_max_child(self, parent_idx):
        """Getting a larger child"""
        raise NotImplementedError

    def __len__(self):
        """Get heap size"""
        return self.size

    def __str__(self):
        return str(self.heap)
        