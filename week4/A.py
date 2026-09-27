class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

n, comms = map(int, input().split())

def insert(node, data):
    new = TreeNode(data)
    if node is None:
        return new
    curr = node
    cnt = 0
    while curr is not None:
        if cnt == 100:
            return node
        if curr.data >= data and curr.left is not None:
            curr = curr.left
        elif curr.data < data and curr.right is not None:
            curr = curr.right
        else:
            break
        cnt += 1
    if curr.data >= data:
        curr.left = new
    else:
        curr.right = new
    return node

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