# Connected, directed graph
# ---------------
# node
#  children[2]
#  numeric (int) user_data

class Node:
    children = []
    user_data = ""
    def __init__(self, children, user_data):
        self.children = children
        self.user_data = user_data

f_node = Node([None, None], '60') # leaf
e_node = Node([f_node, None], '35') # leaf
d_node = Node([None, None], '25') # leaf
c_node = Node([None, f_node], '50') #none, 60
b_node = Node([d_node, e_node], '30') #25, 35
a_node = Node([b_node, c_node], '40') #30,50


#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

#     40
#    /  \
#   30   50
#  /  \    \
# 25   35   60

# 25, 30, 35, 40, 50, 60


"""
def preorder(node):
    if no children then
      print node.user_data
      return
    traverse left side
    traverse right side
"""

def preorder_traversal(node):
    if node is None:
        return
    print(node.user_data)
    preorder_traversal(node.children[0])
    preorder_traversal(node.children[1])
preorder_traversal(a_node)

# preorder_traversal(a_node)
# 'node'==a
#   preorder_traversal(b_node)
#   'node'==b
#     preorder_traversal(d_node)
#     'node'==d
#     return up stack
#   preorder_traversal(e_node)
#   'node'==e 
