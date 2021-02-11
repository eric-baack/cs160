'''Build a ladder of words using stacks and queues'''
#!/usr/bin/env python3

WORDS_OF_3 = set()
WORDS_OF_4 = set()
WORDS_OF_5 = set()


class Stack:
    '''Implementing Stack ADT as a list'''
    def __init__(self):
        '''Initialize an instance'''
        self.items = []

    def is_empty(self):
        '''Is stack empty?'''
        return self.items == []

    def size(self):
        '''Return stack size'''
        return len(self.items)

    def push(self, item):
        '''Add new item to stack'''
        self.items.append(item)

    def pop(self):
        '''Remove an item from stack'''
        return self.items.pop()

    def peek(self):
        '''Look at the top item'''
        return self.items[-1]

    def clone(self):
        '''Cloning a stack'''
        nstack = Stack()
        for ctr in range(len(self.items)):
            nstack.push(self.items[ctr])
        #print(f"cloning {nstack}")
        return nstack

    def __str__(self):
        """str function for Stack"""
        stack_str = ""
        for ctr in range(len(self.items)):
            stack_str = stack_str + self.items[ctr] + " "
        return stack_str


class Queue:
    '''Implementing Queue ADT as a list'''
    def __init__(self):
        '''Initialize an instance'''
        self.items = []

    def is_empty(self):
        '''is the Queue empty'''
        return self.items == []

    def enqueue(self, item):
        '''Add an item'''
        self.items.insert(0, item)

    def dequeue(self):
        '''Remove an item'''
        return self.items.pop()

    def size(self):
        '''How big is it?'''
        return len(self.items)


def read_file(filename: str) -> dict:
    '''Read a file into 3 sets'''
    file_read = open(filename, "r")
    for line in file_read:
        line = line.strip()
        if len(line) == 3:
            WORDS_OF_3.add(line)
        elif len(line) == 4:
            WORDS_OF_4.add(line)
        elif len(line)==5:
            WORDS_OF_5.add(line)


def distance(word1: str, word2: str) -> int:
    '''Differences between words'''
    diff_count = 0
    ctr = 0
    while ctr in range(len(word1)) and diff_count < 2:
        #print(f"word1 {word1}, word2 {word2}")
        if word1[ctr] != word2[ctr]:
            diff_count += 1
        ctr += 1
    return diff_count


def diff_by_one_all(word, all_words, used_words):
    '''Find all words that differ by 1 letter'''
    one_diff_words = []
    for test_word in all_words:
        if test_word not in used_words:
            if distance(word, test_word) == 1:
                one_diff_words.append(test_word)
                used_words[test_word] = 1   # adding to dict, NOT LIST!
    return one_diff_words, used_words


def main():
    '''Main function'''
    read_file('data/projects/words/words.txt')

    word_start = 'stone'
    word_stop = 'water'
    found = False
    if len(word_start) != len(word_stop):
        raise Exception('You have to use words of the same length (3, 4, or 5 letters)')
    if (len(word_start)) == 3:
        words_to_use = WORDS_OF_3
    elif (len(word_start)) == 4:
        words_to_use = WORDS_OF_4
    elif (len(word_start)) == 5:
        words_to_use = WORDS_OF_5
    else:
        raise Exception('You have to use words of the same length (3, 4, or 5 letters)')
    
    print("Let's turn '%s' into '%s'" % (word_start, word_stop))
    used_words = {}  # This is critical!  If list, time to check if in list is O(N).  If dict, O(1)
    one_diff_words = []
    ladder_list = Queue()
    wladder = Stack()
    wladder.push(word_start)
    found = False
    ender = False
    one_diff_words, used_words = diff_by_one_all(word_start, words_to_use, used_words)
    # note:  these lists were not behaving as expected when I did not return them.  Not clear on this.
    # This implementation is not ideal:  as used_list grows, words_to_use does not shrink.  
    # 

    for wctr in one_diff_words:
        nladder = wladder.clone()
        nladder.push(wctr)
        ladder_list.enqueue(nladder)
    lsize = 1  
    while not found and not ender:
        if ladder_list.size() == 0:
            ender = True
        else:
            wladder = ladder_list.dequeue()
            if wladder.size() > lsize:
                print(f"chain length = {wladder.size()}, Queue size = {ladder_list.size()}, # used words = {len(used_words)}")
                lsize = wladder.size()
            if wladder.peek() == word_stop:
                found = True
                fladder = wladder.clone()
                fladder.push(wctr)
            else:
                one_diff_words, used_words = diff_by_one_all(wladder.peek(), words_to_use, used_words)
                for wctr in one_diff_words:
                    if not found:
                        if wctr != word_stop:
                            nladder = wladder.clone()
                            nladder.push(wctr)
                            ladder_list.enqueue(nladder) 
                        else:
                            found = True
                            fladder = wladder.clone()
                            fladder.push(wctr)
        
    if found:
        print('Ladder found!')
        print(f"word ladder:  {fladder}")
        
    else:
        print('Ladder not found')


if __name__ == '__main__':
    main()
    