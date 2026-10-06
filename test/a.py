class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None 
def insert(root, data):
    if root is None:
        return TreeNode(data)
    cur = root 
    cnt = 0
    while True:
        if cnt == 100:
            return root
        elif data <= cur.data:
            if cur.left is None:
                cur.left = TreeNode(data)
                return root 
            cur = cur.left
        else:
            if cur.right is None:
                cur.right = TreeNode(data)
                return root 
            cur = cur.right
        cnt += 1
n, m = map(int, input().split())
tree = None
for i in map(int, input().split()):
    tree = insert(tree, i)
for i in range(m):
    cur = tree 
    for s in input():
        if cur is None:
            break 
        elif s == "L":
            cur = cur.left 
        else:
            cur = cur.right 
    if cur:
        print("YES")
    else:
        print("NO")