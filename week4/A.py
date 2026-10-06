class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

n, comms = map(int, input().split())

def insert(root, data):
    if root is None:
        return TreeNode(data)
    curr = root
    cnt = 0
    while True:
        if cnt == 100:
            return root
        if data <= curr.data:
            if curr.left is None:
                curr.left = TreeNode(data) 
                return root 
            curr = curr.left
        else:
            if curr.right is None:
                curr.right = TreeNode(data) 
                return root 
            curr = curr.right
        cnt += 1

tree = None
for i in map(int, input().split()):
    tree = insert(tree, i)

for i in range(comms):
    current = tree
    for s in input():
        if current is None:
            break
        elif s == "L":
            current = current.left
        elif s == "R":
            current = current.right
    if current is None:
        print("NO")
    else:
        print("YES")