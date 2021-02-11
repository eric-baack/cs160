"""Morse code encoding and decoding"""
#!/usr/bin/env python3
# encoding: UTF-8

# Key insights.  1.  Coder is not a tree, but it includes a tree.  Create tree in __init__
#  2.  When accessing tree, do NOT do this:  self.tree = self.tree.get_right_child().   
# This will change the tree.  Instead, use a temporary variable, current_tree, to move through tree.
# 3.  Find_path recursion was failing because when second option was tried ("-"), the residue of first
# option was still present.  Need to have 'old path' and 'old tree' to ensure clean start on second option.

# from src.notes.trees.BinaryTree import BinaryTree  ## failed!

from pythonds3.trees import BinaryTree  


class Coder:
    """Morse Code Encoder/Decoder"""

    def __init__(self, file_in: str):
        self.morse_tree = BinaryTree("*")   # key step!
        file_read = open(file_in, "r")
        for line in file_read:
            cstr = line.split()
            letter = cstr[0]
            code = cstr[1]
            self.follow_and_insert(code, letter)

    def follow_and_insert(self, code_str: str, letter: str):  # not quite working!
        """Follow the tree and insert a letter"""
        current_tree = self.morse_tree
        for dctr in range(len(code_str)):
            if code_str[dctr] == ".":
                if current_tree.get_child_left() is None:
                    current_tree.insert_left(None)
                if dctr == len(code_str) - 1:
                    current_tree.get_child_left().set_root_val(letter)
                else:
                    current_tree = (
                        current_tree.get_child_left()
                    )  # This was problem when using self.tree!
            if code_str[dctr] == "-":
                if current_tree.get_child_right() is None:
                    current_tree.insert_right(None)
                if dctr == len(code_str) - 1:
                    current_tree.get_child_right().set_root_val(letter)
                else:
                    current_tree = (
                        current_tree.get_child_right()
                    )  # key:  temporary tree!

    def follow_and_retrieve(self, code_str: str):
        """Follow the tree and retrieve a letter"""
        cletter = ""
        tree = self.morse_tree
        for cctr in range(len(code_str)):
            if code_str[cctr] == ".":
                if cctr == len(code_str) - 1:
                    if tree.get_child_left() is not None:
                        cletter = tree.get_child_left().get_root_val()
                else:
                    if tree.get_child_left() is not None:
                        tree = tree.get_child_left()
            if code_str[cctr] == "-":
                if cctr == len(code_str) - 1:
                    if tree.get_child_right() is not None:
                        cletter = tree.get_child_right().get_root_val()
                else:
                    if tree.get_child_right() is not None:
                        tree = tree.get_child_right()
        return cletter

    def find_path(self, tree: object, letter: str, path: str):
        """Find a key"""
        scode = ""
        for handctr in range(2):
            if handctr == 0:
                opath = path  ## Necessary to start from beginning with -
                old_tree = tree  ## this as well.
                path = path + "."
                if tree.get_child_left() is not None:
                    # print(f"path {path} letter {tree.get_child_left().get_root_val()}")
                    if letter == tree.get_child_left().get_root_val():
                        scode = path
                    else:
                        tree = tree.get_child_left()
                        scode = self.find_path(tree, letter, path)
            else:
                path = opath + "-"
                opath = path
                tree = old_tree
                old_tree = tree
                if tree.get_child_right() is not None:
                    if letter == tree.get_child_right().get_root_val():
                        scode = path
                    else:
                        tree = tree.get_child_right()
                        scode = self.find_path(tree, letter, path)
            if len(scode) > 0:
                return scode
        else:
            return ""

    def encode(self, msg: str):
        """Encode a message"""
        code_str = ""
        msg = msg.replace(" ", "")
        for lctr in range(len(msg)):
            cletter = msg[lctr]
            path = ""
            lcode = ""
            lcode = self.find_path(self.morse_tree, cletter, path)
            if len(lcode) > 0:
                code_str = code_str + lcode + " "
            else:
                raise ValueError(f"Could not encode {msg}: {msg[0]} is not in the tree")
        return code_str

    def decode(self, code: str):
        """Decode a message"""
        clist = code.split()
        lcode = ""
        for mctr in range(len(clist)):
            nletter = self.follow_and_retrieve(clist[mctr])
            if len(nletter) == 1:
                lcode = lcode + nletter
            else:
                raise ValueError(f"Could not decode {code}: {code} is not in the tree")
        return lcode


def main():
    morse_coder = Coder("data/projects/morse/morse.txt")
    print("Encoding 'sos'")
    print("Expected: ... --- ...")
    print("Encoded :{}".format(morse_coder.encode("sos")))
    print("---")
    print("Encoding 'data structures'")
    print("Expected: -.. .- - .- ... - .-. ..- -.-. - ..- .-. . ... ")
    print("Encoded :{}".format(morse_coder.encode("data structures")))
    print("---")
    print("Encoding '$$'")
    print("Expected: Error message")
    try:
        print("Encoded :{}".format(morse_coder.encode("$$")))
    except ValueError as ve:
        print("ERROR: {}".format(ve))
    print("---")
    print("Decoding '.... . .-.. .-.. --- --..-- -.-. ... .---- -.... -----'")
    print("Expected: hello,cs160")
    test_str = ".... . .-.. .-.. --- --..-- -.-. ... .---- -.... -----"
    print("Decoded : {}".format(morse_coder.decode(test_str)))


if __name__ == "__main__":
    main()
