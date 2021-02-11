"""Tree building exercise"""
#!/usr/bin/env python3


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

    def clockwise(self):
        """Clockwise tree traversal"""
        print(self._key, end=" ")
        if self._child_right:
            self._child_right.clockwise()
        if self._child_left:
            self._child_left.clockwise()

    def height(self):
        """Obtain the height of a tree """
        if self.get_child_left() is not None:
            Lheight = 1 + self.get_child_left().height()
        else:
            Lheight =  0
        if self.get_child_right() is not None:
            Rheight = 1 + self.get_child_right().height()
        else:
            Rheight = 0
        return max(Lheight, Rheight)



def build_tree_lst() -> object:
    """Build a tree and return it"""
    myTree = ['a', ['b', [],['d']],['c',['e'], ['f'] ]]
    return myTree

    

def build_tree_oop() -> object:
    """ Build a tree using nodes and return it"""
    myTree = BinaryTree('a')
    myTree.insert_left('b')
    myTree.insert_right('c')
    myTree.get_child_left().insert_right('d')
    myTree.get_child_right().insert_left('e')
    myTree.get_child_right().insert_right('f')
    return myTree

def preorder(tree):
    if tree:
        print(tree.get_root_val())
        preorder(tree.get_child_left())
        preorder(tree.get_child_right())

def postorder(tree):
     if tree:
        postorder(tree.get_child_left())
        postorder(tree.get_child_right())
        print(tree.get_root_val())
        

def inorder(tree):
     if tree:
        inorder(tree.get_child_left())
        print(tree.get_root_val())
        inorder(tree.get_child_right())
        
def main():
    myTree = build_tree_oop()
    print("preorder")
    preorder(myTree)
    print("postorder")
    postorder(myTree)
    print("inorder")
    inorder(myTree)
    print(f"height {myTree.height()}")

if __name__ == "__main__":
    main()