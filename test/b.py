class TreeNode:
    def __init__ (self, data):
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
def bfs(root):
    q = [root]
    cnt = 0
    while q:
        node = q[0]
        q = q[1: ]
        cnt += 1
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return cnt
n = int(input())
tree = None
for i in map(int, input().split()):
    tree = insert(tree, i)
k = int(input())
cur = tree
while cur.data != k:
    if k < cur.data:
        cur = cur.left
    else:
        cur = cur.right
print(bfs(cur))