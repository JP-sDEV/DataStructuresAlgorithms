from Binary_Tree import BinaryTree

class LinkedBinaryTree(BinaryTree):
    
    # ----- linked representation of a binary tree structure ----- #

    # ----- class for storing node in tree ----- #
    class _Node:

        __slots__ = "_element", "_parent", "_left", "_right"
        def __init__(self, element, parent = None, left = None, right = None):
            self._element = element 
            self._parent = parent 
            self._left = left
            self._right = right
    
    # ----- abstraction for representing location of single element in tree ----#
    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            self._container = container
            self._node = node
        
        def element(self):
            return self._node._element
        
        def __eq__(self, other):
            """ return True if other represents the same location """
            return type(other) is type(self) and other._node is self._node
    
    # ----- helper/utility methods implemented in this class ----- #
    def _validate(self, p):
        """ return p's associated node if postion if valid """
        if not isinstance(p, self.Position):
            raise TypeError("p must be a proper Position type")

        if p._container is not self:
            raise ValueError("p does not beling to this container")

        if p._node._parent is p._node:
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        """ return Position instance for given Node """
        # assign the node a position, make it accessible
        return self.Position(self, node) if node is not None else None
    
    # ----- binary tree constructor ----- #
    def __init__(self):
        """ initially create an empty binary tree """
        self._root = None
        self._size = 0
    
    # ---- public accessors ----- #
    """ get binary tree info """

    def __len__(self):
        return self._size
    
    def root(self):
        """ return root Position of tree (None, if tree is empty) """
        return self._make_position(self._root)

    def parent(self, p):
        """ return the Position of p's parent """
        node = self._validate(p)
        return self._make_position(node._parent)
    
    def left(self, p):
        """ return the Position of p's left child  """
        node = self._validate(p)
        return self._make_position(node._left)
    
    def right(self, p):
        """ return the Position of p's right child  """
        node = self._validate(p)
        return self._make_position(node._right)
    
    def num_children(self, p):
        node = self._validate(p)
        count = 0 
        if node._left is not None:
            count += 1

        if node._right is not None: 
            count += 1

        return count
    
    def _add_root(self, e):
        if self._root is not None: 
            raise ValueError("Root exists")

        self._size += 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError("Left child exists")

        self._size += 1 
        # create a _Node instance and assign it as parent left child
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError("Right child exists")

        self._size += 1 
        # create a _Node instance and assign it as parent left child
        node._right = self._Node(e, node)
        return self._make_position(node._right)
    
    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old
    
    def _delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError("p  has two children")

        # p must have 1 child (left or right)
        child = node._left if node._left else node._right
        
        if child is not None:
            # reassign child's parent to the node's parent, i.e.) child's "grandparent"
            child._parent = node._parent
        
        if node is self._root:
            self._root = child
        
        else:
            
            # reassign child in parent node 
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        
        self._size -= 1
        
        # deprecating deleted node
        node._parent = node

        return node._element
    
    def _attach(self, p, t1 , t2):
        node = self._validate(p)
        
        if not self.is_leaf(p):
            raise ValueError("position must be leaf")

        if not type(self) is type(t1) is type(t2):
            raise TypeError("Tree types must match")

        self._size += len(t1) + len(t2)

        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0

        if not t2.is_empty():
            t2._root._parent = node
            node._left = t2._root
            t2._root = None
            t2._size = 0        

sample_binary_tree = LinkedBinaryTree()

root = sample_binary_tree._add_root("3")
print (sample_binary_tree.root().element())

sample_binary_tree._add_left(root, "1")
sample_binary_tree._add_right(root, "7")

left = sample_binary_tree.left(root).element()
right = sample_binary_tree.right(root).element()
print ("number of tree elements: {}".format(sample_binary_tree.__len__()))
print ("number of children: {}".format(sample_binary_tree.num_children(root)))
print ("left: {}\nright: {}".format(left, right))
