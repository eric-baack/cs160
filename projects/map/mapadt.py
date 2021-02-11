"""Implementation of the Map ADT as HashTable"""

# March 23, 2019.  First try.  Test_mapadt.py is not functioning
# Apr 3.  Now mostly working.
# Rehash function needed to be r = h + step**2, not r = r + step ** 2


class HashTable:
    """ HashTable"""

    def __init__(self, size_init: int = 16):
        """Constructor"""
        self._size = size_init
        self._keys = [None] * self._size
        self._values = [None] * self._size

    def __getitem__(self, key: int):
        """__getitem__"""
        return self.get(key)

    def __setitem__(self, key: int, value):
        """__setitem__"""
        self.put(key, value)

    def __len__(self):
        """__len__"""
        klist = self.keys()  # remember - this is a function!
        item_ctr = 0
        for i in klist:
            item_ctr += 1
        return item_ctr

    def len(self):
        return self.__len__

    def __contains__(self, key):
        """__contains__"""
        data = self.__getitem__(key)
        data_found = True
        if data is None:
            data_found = False
        return data_found

    def __str__(self):  ## need to remove final comma
        """__str__"""
        maplist = "{"
        first = True
        for i in self.items():
            if not first:
                maplist = maplist + ", "
            maplist = maplist + str(i[0]) + ": "
            maplist = maplist + "'" + i[1] + "'"
            if first:
                first = False
        maplist = maplist + "}"
        return maplist

    def _hash(self, key: int, size: int):
        """Simple hash function"""
        return key % size

    def _rehash(self, old_hash: int, size: int, step: int = 1):
        """Quadratic rehash"""
        return (old_hash + step ** 2) % size

    def put(self, key: int, value):
        """Add or update an item"""
        hashvalue = self._hash(key, len(self._keys))

        if self._keys[hashvalue] is None:
            self._keys[hashvalue] = key
            self._values[hashvalue] = value
        else:
            if self._keys[hashvalue] == key:
                self._values[hashvalue] = value  # replace
            else:
                nextslot = self._rehash(hashvalue, len(self._keys))
                hctr = 0
                while self._keys[nextslot] is not None and self._keys[nextslot] != key:
                    nextslot = self._rehash(hashvalue, len(self._keys), hctr + 2)
                    hctr += 1
                    if hctr == len(self._keys):
                        raise Exception("Hash Table is full")

                if self._keys[nextslot] is None:
                    self._keys[nextslot] = key
                    self._values[nextslot] = value
                else:
                    self._values[nextslot] = value  # replace

    def get(self, key: int):
        """Retrieve an item"""
        startslot = self._hash(key, len(self._keys))

        data = None
        stop = False
        found = False
        position = startslot
        rehashctr = 1
        while self._keys[position] is not None and not found and not stop:
            if self._keys[position] == key:
                found = True
                data = self._values[position]
            else:
                position = self._rehash(startslot, len(self._keys), rehashctr)
                if rehashctr > len(self._keys):
                    stop = True
                else:
                    rehashctr += 1
        return data

    def keys(self):
        """Return all keys"""
        key_list = []
        for ctr in range(self._size):
            if self._keys[ctr] is not None:
                key_list.append(self._keys[ctr])
        return key_list

    def values(self):
        """Return all values"""
        values_list = []
        for ctr in range(self._size):
            if self._keys[ctr] is not None:
                values_list.append(self._values[ctr])
        return values_list

    def items(self):
        """Return all items"""
        tuples_list = []
        for ctr in range(self._size):
            if self._keys[ctr] is not None:
                tuples_list.append((self._keys[ctr], self._values[ctr]))
        return tuples_list


def main():

    AMap = HashTable(11)
    map_test_items = [
        (54, "aardvark"),
        (26, "beaver"),
        (93, "cheetah"),
        (17, "dolphin"),
        (77, "elephant"),
        (31, "flamingo"),
        (44, "goat"),
        (55, "hippo"),
        (20, "iguana"),
    ]
    for item in map_test_items:
        AMap.put(item[0], item[1])
    AMap.put(21, "jackal")
    print(AMap._keys)
    AMap.put(18, "koala")
    print(AMap._keys)
    # print(AMap._keys)
    # print(AMap._values)
    # print(AMap.len())
    # print(AMap.items())


if __name__ == "__main__":
    main()
