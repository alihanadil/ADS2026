class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def insert(root, data):
    if root is None:
        return TreeNode(data)
    cur = root 
    while True:
        if data < cur.data:
            if cur.left is None:
                cur.left = TreeNode(data)
                return root 
            cur = cur.left
        else:
            if cur.right is None:
                cur.right = TreeNode(data)
                return root 
            cur = cur.right 

def preorder(root):
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
cur = tree
k = int(input())
while k != cur.data:
    if k < cur.data:
        cur = cur.left 
    else:
        cur = cur.right 
preorder(cur)