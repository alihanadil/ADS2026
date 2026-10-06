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
def bfs(root):
    current = [root]
    sums = []
    level = 0
    while current:
        len_lvl = len(current)
        new = []
        s = 0
        for _ in range(len_lvl):
            node = current.pop()
            s += node.data
            if node.left:
                new.append(node.left)
            if node.right:
                new.append(node.right)
        sums.append(s)
        current = new
        level += 1
    print(level)
    print(' '.join(map(str, sums)))
n = int(input())
tree = None
for i in map(int, input().split()):
    tree = insert(tree, i)
bfs(tree)