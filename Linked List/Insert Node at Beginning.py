class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next



def insertAtFirst(list: Node, newValue: int) -> Node:
    n_node=Node(newValue)
    n_node.next=list
    list=n_node
    return list
