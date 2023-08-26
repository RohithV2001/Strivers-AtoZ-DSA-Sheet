class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
 
# Function to print all nodes of a
# binary tree in Preorder, Postorder
# and Inorder using only one stack
def allTraversal(root):
   
    # Stores preorder traversal
    pre = []
 
    # Stores inorder traversal
    post = []
 
    # Stores postorder traversal
    inn = []
 
    # Stores the nodes and the order
    # in which they are currently visited
    s = []
 
    # Push root node of the tree
    # into the stack
    s.append([root, 1])
 
    # Traverse the stack while
    # the stack is not empty
    while (len(s) > 0):
 
        # Stores the top
        # element of the stack
        p = s[-1]
        #del s[-1]
 
        # If the status of top node
        # of the stack is 1
        if (p[1] == 1):
 
            # Update the status
            # of top node
            s[-1][1] += 1
 
            # Insert the current node
            # into preorder, pre[]
            pre.append(p[0].data)
 
            # If left child is not NULL
            if (p[0].left):
 
                # Insert the left subtree
                # with status code 1
                s.append([p[0].left, 1])
 
        # If the status of top node
        # of the stack is 2
        elif (p[1] == 2):
 
            # Update the status
            # of top node
            s[-1][1] += 1
 
            # Insert the current node
            # in inorder, in[]
            inn.append(p[0].data);
 
            # If right child is not NULL
            if (p[0].right):
 
                # Insert the right subtree into
                # the stack with status code 1
                s.append([p[0].right, 1])
 
        # If the status of top node
        # of the stack is 3
        else:
 
            # Push the current node
            # in post[]
            post.append(p[0].data);
 
            # Pop the top node
            del s[-1]
 
    print("Preorder Traversal: ",end=" ")
    for i in pre:
        print(i,end=" ")
    print()
 
    # Printing Inorder
    print("Inorder Traversal: ",end=" ")
 
    for i in inn:
        print(i,end=" ")
    print()
 
    # Printing Postorder
    print("Postorder Traversal: ",end=" ")
 
    for i in post:
        print(i,end=" ")
    print()
 
 
# Driver Code
if __name__ == '__main__':
 
    # Creating the root
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
 
    # Function call
    allTraversal(root)
