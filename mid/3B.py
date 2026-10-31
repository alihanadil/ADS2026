class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None 
def insert(root, data):
    if root is None:
        return TreeNode(data)
    curr = root
    while True:
        if curr.data == data:
            return root
        elif curr.data > data:
            if curr.left is None:
                curr.left = TreeNode(data)
                return root 
            curr = curr.left 
        else:
            if curr.right is None:
                curr.right = TreeNode(data)
                return root 
            curr = curr.right
def dfs(root):
    current = [root]
    cnt = 0
    while current:
        len_lvl = len(current)
        cnt += 1
        new = []
        for _ in range(len_lvl):
            node = current.pop()
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
print(dfs(tree))