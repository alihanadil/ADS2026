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
    num = 0
    while current:
        len_lvl = len(current)
        new = []
        for _ in range(len_lvl):
            node = current.pop()
            if node.left and node.right:
                num += 1
            if node.left:
                new.append(node.left)
            if node.right:
                new.append(node.right)
        current = new 
    return num
n = int(input())
tree = None
for i in map(int, input().split()):
    tree = insert(tree, i)
print(bfs(tree))