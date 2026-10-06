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

def smallest(root, k):
    if root is None:
        return None
    cur = root 
    stack = []
    small = []
    while cur is not None:
        stack.append(cur)
        cur = cur.left
        while cur is None and stack:
            node = stack.pop()
            small.append(node.data)
            cur = node.right
    print(small[k - 1])
n, m = map(int, input().split())
tree = None
for i in map(int, input().split()):
    tree = insert(tree, i)
if n >= m:
    smallest(tree, m)
else:
    print(-1)