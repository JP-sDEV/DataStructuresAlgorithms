from Tree import Tree

# ----- abstract base class of binary tree structure ----- #
class BinaryTree(Tree):

    # ----- additional abstract methods ----- #
    def left(self, p):
        raise NotImplementedError("must be implemented by subclass")

    def right(self,p):
        raise NotImplementedError("must be implemented by subclass")

# ----- concrete methods implemented in this class ----- #
    def sibling(self, p):
        """ return the Position for p's sibling """
        parent = self.parent(p)
        if parent is None:
            return None
        
        else:
            if p == self.left(parent):
                return self.right(parent)
            
            else:
                return self.left(parent)
    
    def children(self, p):
        """ return the Position p's left and right child (if they exist) """
        if self.left(p) is not None:
            yield self.left(p)

        if self.right(p) is not None:
            yield self.right(p)