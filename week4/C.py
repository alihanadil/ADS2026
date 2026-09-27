class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(node, data):
    new = TreeNode(data)
    if node is None:
        return new
    curr = node
    while curr is not None:
        if curr.data >= data and curr.left is not None:
            curr = curr.left 
        elif curr.data < data and curr.right is not None:
            curr = curr.right 
        else:
            break
    if curr.data >= data:
        curr.left = new
    elif curr.data < data:
        curr.right = new
    return node 

def preorder(root):
    if root is None:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.data, end=" ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
            
n = int(input())
tree = None
for i in map(int, input().split()):
    tree = insert(tree, i)
target = int(input())
cur = tree
while cur.data != target:
    if target > cur.data:
        cur = cur.right 
    elif target < cur.data:
        cur = cur.left
preorder(cur)