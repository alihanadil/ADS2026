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

def bfs(root):
    q = []
    q.append(root)
    cnt = 0
    while q:
        node = q[0]
        q = q[1 : ]
        cnt += 1
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return cnt
def getSize(root):
    if root is None:
        return 0
    return bfs(root)

n = int(input())
tree = None
for i in map(int, input().split()):
    tree = insert(tree, i)
x = int(input())
curr = tree

while curr.data != x:
    if x > curr.data:
        curr = curr.right 
    elif x < curr.data:
        curr = curr.left
print(getSize(curr))
