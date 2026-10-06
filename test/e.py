class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bfs(root):
    current = [root]
    size = 0
    while current:
        len_lvl = len(current)
        new = []
        for _ in range(len_lvl):
            node = current.pop()
            if node.left:
                new.append(node.left)
            if node.right:
                new.append(node.right)
        current = new
        if len_lvl > size:
            size = len_lvl
    return size

n = int(input())
nodes = [TreeNode(i) for i in range(1, n + 1)]
for i in range(n - 1):
    x, y, z = map(int, input().split())
    if z == 1:
        nodes[x - 1].right = nodes[y - 1]
    else:
        nodes[x - 1].left = nodes[y - 1]
print(bfs(nodes[0]))