"""Tree: module level docstring."""

class ListTree:
    """"""
    pass

class Tree:
    """"""
    def __init__(self, root_obj=None, payload=None, children = []):
        self.key = root_obj
        self.children = children
    
    def append_child(self, ):
        """"""
        pass

    def insert_child(self, ):
        """"""
        pass
    
    def get_child(self, ):
        """"""
        pass
    
    def get_children(self, ):
        """"""
        pass
    
    def set_root_value(self, ):
        """"""
        pass
    
class BinaryTree:
    """"""
    def __init__(self, payload=None, parent=None, left_child=None, right_child=None):
        """"""
        self.payload = payload
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child

    def __init__ (self, root_payload=None):
        self.root = TreeNode(root_payload)
        self.depth = 0
    
    def insert_lchild(self, node, left_child):
        """"""
        node.left_child = left_child
        
    def insert_rchild(self, node, right_child):
        """"""
        node.right_child = right_child
        
    def del_lchild(self, node, left_child):
        """"""
        node.left_child = None
        
    def del_rchild(self, node, right_child):
        """"""
        node.right_child = None
        
    def del_rchild(self, node, right_child):
        """"""
        node.right_child = None
        
    def del_rchild(self, node, right_child):
        """"""
        node.right_child = None

class Heap:
    """"""
    pass

class BST:
    """"""
    pass

class AVL:
    """"""
    pass