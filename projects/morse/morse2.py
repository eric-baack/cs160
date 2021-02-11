"""Morse code encoding and decoding"""
#!/usr/bin/env python3
# encoding: UTF-8

class BinaryTree:
    """Binary Tree implementation as nodes and references"""

    def __init__(self, key):
        self._key = key
        self._child_left = None
        self._child_right = None

    def get_root_val(self):
        """Get root key value"""
        return self._key

    def set_root_val(self, new_key):
        """Set root key value"""
        self._key = new_key

    def get_child_left(self):
        """Get left child"""
        return self._child_left

    def set_child_left(self, new_child_left):
        """Set left child"""
        self._child_left = new_child_left

    def get_child_right(self):
        """Get right child"""
        return self._child_right

    def set_child_right(self, new_child_right):
        """Set right child"""
        self._child_right = new_child_right

    def is_leaf(self):
        """Check if a node is leaf"""
        return (not self._child_left) and (not self._child_right)

    def insert_left(self, new_node):
        """Insert left subtree"""
        new_subtree = BinaryTree(new_node)
        if self._child_left != None:
            new_subtree.set_child_left(self._child_left)
        self._child_left = new_subtree

    def insert_right(self, new_node):
        """Insert right subtree"""
        new_subtree = BinaryTree(new_node)
        if self._child_right != None:
            new_subtree.set_child_right(self._child_right)
        self._child_right = new_subtree

    def preorder(self):
        """Pre-order tree traversal"""
        print(self._key, end=" ")
        if self._child_left:
            self._child_left.preorder()
        if self._child_right:
            self._child_right.preorder()

    def inorder(self):
        """In-order tree traversal"""
        if self._child_left:
            self._child_left.inorder()
        print(self._key, end=" ")
        if self._child_right:
            self._child_right.inorder()

    def postorder(self):
        """Post-order tree traversal"""
        if self._child_left:
            self._child_left.postorder()
        if self._child_right:
            self._child_right.postorder()
        print(self._key, end=" ")

class Coder:
    """Morse Code Encoder/Decoder"""

    def __init__(self, file_in: str):
        self.tree = BinaryTree("*")
        file_read = open(file_in, "r")
        for line in file_read:
            cstr = line.split()
            letter = cstr[0]
            code = cstr[1]
            self.follow_and_insert(code, letter)  

    def follow_and_insert(self, code_str: str, letter: str):
        """Follow the tree and insert a letter"""
        newtree = self.tree
        print(f"{self.tree.preorder()}")
        for dctr in range(len(code_str)):
            if code_str[dctr] == ".":
                if self.tree.get_child_left() == None:
                    self.tree.insert_left("Q")
                if dctr == len(code_str) - 1:
                    self.tree.get_child_left().set_root_val(letter)
                else:
                    self.tree = self.tree.get_child_left()  # suspect problem here
            if code_str[dctr] == "-":
                if self.tree.get_child_right() == None:
                    self.tree.insert_right("Q")
                if dctr == len(code_str) - 1:
                    self.tree.get_child_right().set_root_val(letter)
                else:
                    self.tree = self.tree.get_child_right()  # and here.  Not moving down tree.


    def follow_and_retrieve(self, code_str: str):
        """Follow the tree and retrieve a letter"""
        if code_str[0] == ".":
            if len(code_str) == 1:
                cletter = self.tree.get_child_left().get_root_val(letter)
            else:
                self.tree = self.get_child_left()
                self.follow_and_retrieve(code_str[1:])
        if code_str[0] == "-":
            if len(code_str) == 1:
                cletter = self.tree.get_child_right().get_root_val(letter)
            else:
                self.tree = self.tree.get_child_right()
                self.follow_and_retrieve(code_str[1:])
        return cletter  

    def find_path(self, tree: object, letter: str, path: str): 
        """Find a key"""
        lfound = False
        self.tree = tree
        if len(path) < 7 and not lfound:
            print(f"path {path}")
            if path[len(path)-1] == ".":   ## Crashing here - no branch on tree
                if self.tree.get_child_left != None:
                    print(f"letter {self.tree.get_child_left().get_root_val()}")
                    if letter == self.tree.get_child_left().get_root_val():
                        lfound = True
                    else:
                        pathl = path + "."
                        self.tree = self.tree.get_child_left()
                        self.find_path(self.tree, letter, pathl)
                        pathr = path + "-"
                        self.tree = self.tree.get_child_left()
                        self.find_path(self.tree, letter, pathr)
            if path[len(path)-1] == "-":
                if self.tree.get_child_right != None:
                    print(f"letter {self.tree.get_child_right.get_root_val()}")
                    if letter == self.tree.get_child_right().get_root_val():
                        lfound = True
                    else:
                        pathl = path + "."
                        self.tree = self.get_child_right()
                        self.find_path(self.tree, letter, pathl)
                        pathr = path + "-"
                        self.tree  = self.tree.get_child_right()
                        self.find_path(self.tree, letter, pathr)
            if len(path) == 7:
                return "X"
        else:
            return path


    def encode(self, msg: str):
        """Encode a message"""
        code_str = ""
        for lctr in range(len(msg)):
            cletter = msg[lctr]
            path = "."
            lcode = self.find_path(self.tree, cletter, path)
            if lcode == "X":
                path = "-"
                lcode = self.find_path(self.tree, cletter, path)
            code_str = code_str + " " + lcode
        return code_str

    def decode(self, code: str):
        """Decode a message"""
        clist = code.split()
        lcode = ""
        for mctr in range(len(clist)):
            lcode = lcode + self.follow_and_retrieve(clist[mctr])
        return lcode

def main():
    morse_coder = Coder("data/projects/morse/morse.txt")
    print(f"Tree {morse_coder.tree.preorder()}")
    print("Encoding 'sos'")
    print("Expected: ... --- ...")
    print("Encoded : {}".format(morse_coder.encode("sos")))
    print("---")
    print("Encoding 'data structures'")
    print("Expected: -.. .- - .- ... - .-. ..- -.-. - ..- .-. . ... ")
    print("Encoded : {}".format(morse_coder.encode("data structures")))
    print("---")
    print("Encoding '$$'")
    print("Expected: Error message")
    try:
        print("Encoded : {}".format(morse_coder.encode("$$")))
    except ValueError as ve:
        print("ERROR: {}".format(ve))
    print("---")
    print("Decoding '.... . .-.. .-.. --- --..-- -.-. ... .---- -.... -----'")
    print("Expected: hello,cs160")
    test_str = ".... . .-.. .-.. --- --..-- -.-. ... .---- -.... -----"
    print("Decoded : {}".format(morse_coder.decode(test_str)))


if __name__ == "__main__":
    main()
    