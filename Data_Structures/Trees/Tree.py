class Tree:

# ----- abstraction of location of a single element ----- #
    class Position: 
        
        def element(self):
            raise NotImplementedError ('must be implemented by subclass')

        def __eq__(self, other):
            raise NotImplementedError ('must be implemented by subclass')

        def __ne__(self, other):
            raise NotImplementedError ('must be implemented by subclass')

# ----- abstract methods to be defined by subclass ----- # 
    def root(self):
        """ return Position of tree's root """
        raise NotImplementedError ('must be implemented by subclass')

    def parent(self,p):
        """ return parent Position of position p """
        raise NotImplementedError ('must be implemented by subclass')

    def num_children(self,p):
        raise NotImplementedError ('must be implemented by subclass')

    def children(self,p):
        raise NotImplementedError ('must be implemented by subclass')

    def __len__(self):
        raise NotImplementedError ('must be implemented by subclass')

# ----- concrete methods implemented in this class ----- #
    def is_root(self,p):
        return self.root() == p

    def is_leaf(self,p):
        return self.num_children(p) == 0
    
    def is_empty(self,p):
        return len(self) == 0