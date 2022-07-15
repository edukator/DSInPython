class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        current=self.root
        parent=None
        dir=None
        while(current):
            if (current.value>new_val):
                parent=current
                dir="L"
                current=current.left
            else:
                parent=current
                dir="R"
                current=current.right

        if (dir=="L"):
            parent.left=Node(new_val)
        else:
            parent.right=Node(new_val)



    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if(start!=None):
            traversal+=(str(start.value)+"-")
        
            traversal=self.preorder_print(start.left,traversal)
        
            traversal=self.preorder_print(start.right,traversal)
        return traversal



    def level_order_print(self,start,traversal):
        visited=[start]
        current=visited.pop(0)
        traversal=""
        while(True):
            traversal+=(str(current.value)+ "-")
            has_leaf=False
            if(current.left):
                visited.append(current.left)
                has_leaf=True
            if(current.right):
                visited.append(current.right)
                has_leaf=True
            if(len(visited)!=0):
                current=visited.pop(0)
            else:
                break

        return traversal

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        #return self.preorder_print(tree.root, "")[:-1]
        return self.level_order_print(tree.root, "")[:-1]

    def get_height(self):
        visited=[self.root]
        levels=[0]
        current=visited.pop(0)
        cl=levels.pop(0)
        while(True):
            
            has_leaf=False
            if(current.left):
                visited.append(current.left)
                levels.append(cl+1)
                has_leaf=True
            if(current.right):
                visited.append(current.right)
                levels.append(cl+1)
                has_leaf=True
            if(len(visited)!=0):
                current=visited.pop(0)
                cl=levels.pop(0)
            else:
                break

        return cl


    def search(self, find_val):

        current=self.root
        while(current):
            if(current.value==find_val):
                return True
            elif(current.value>find_val):
                current=current.left
            else:
                current=current.right



        return False

    
    
# Set up tree
tree = BST(3)

# Insert elements

tree.insert(5)
tree.insert(2)
tree.insert(1)
tree.insert(4)
tree.insert(6)
tree.insert(7)


print(tree.print_tree())
print(tree.get_height())
# Check search
# Should be True
#print (tree.search(4))
# Should be False
#print (tree.search(6))
