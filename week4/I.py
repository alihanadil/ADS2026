n = int(input())
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    new = TreeNode(data)
    if not root:
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

def bfs(root):
    if root is None:
        return
    current = [root]
    leaves = 0
    while current:
        len_lvl = len(current)
        new = []
        for i in range(len_lvl):
            node = current.pop()
            if node.left:
                new.append(node.left)
            if node.right:
                new.append(node.right)
            if node.right is None and node.left is None:
                leaves += 1
        current = new
    print(leaves)

tree = None
lst = list(map(int, input().split()))
for i in lst:
    tree = insert(tree, i)
bfs(tree)