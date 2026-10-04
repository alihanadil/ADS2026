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
    while True:
        if data < curr.data:
            if curr.left is None:
                curr.left = new
                return node
            curr = curr.left 
        else:
            if curr.right is None:
                curr.right = new
                return node
            curr = curr.right

def bfs(root):
    if not root:
        return 0
    current = [root]
    cnt = 0
    while current:
        len_lvl = len(current)
        new = []
        for i in range(len_lvl):
            node = current.pop()
            if node.left and node.right:
                cnt += 1
            if node.left:
                new.append(node.left)
            if node.right:
                new.append(node.right)
        current = new
    return cnt
n = int(input())
tree = None
for i in map(int, input().split()):
    tree = insert(tree, i)
print(bfs(tree))