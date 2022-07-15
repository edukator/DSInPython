from sqlalchemy import true


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None







class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, current, find_val):
        if current:
            if current.value == find_val:
                return True
            elif current.value < find_val:
                return self.search_helper(current.right, find_val)
            else:
                return self.search_helper(current.left, find_val)
        return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if(start!=None):
            traversal+=(str(start.value)+"-")
        
            traversal=self.preorder_print(start.left,traversal)
        
            traversal=self.preorder_print(start.right,traversal)
        return traversal

    
    def height_recursive(self,start):
        if (start):
            return 1+max(self.height_recursive(start.left),self.height_recursive(start.right))
        return -1


    def get_height(self):
        return  self.height_recursive(self.root)
            



    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return self.preorder_print(tree.root, "")[:-1]
       

    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)


print(tree.get_height())
print(tree.print_tree())

# Check search
# Should be True
print (tree.search(4))
# Should be False
print (tree.search(6))

