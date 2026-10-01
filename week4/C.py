class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    new = TreeNode(data)
    if root is None:
        return new
    curr = root
    while True:
        if data < curr.data:
            if curr.left is None:
                curr.left = new 
                return root 
            curr = curr.left
        else:
            if curr.right is None:
                curr.right = new 
                return root 
            curr = curr.right

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