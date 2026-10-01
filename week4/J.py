# 1
n, k = map(int, input().split())
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

def smallest(root, k):
    if root is None:
        return None 
    stack = [root]
    small = []
    while stack:
        node = stack.pop()
        small.append(node.data)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    small.sort()
    # print(small)
    print(small[k - 1])
tree = None
lst = list(map(int, input().split()))
for i in lst:
    tree = insert(tree, i)
if n >= k:
    smallest(tree, k)
else:
    print(-1)

# 2
n, k = map(int, input().split())
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
        elif data > curr.data:
            if curr.right is None:
                curr.right = new
                return root
            curr = curr.right
        else:
            return root

def smallest(root, k):
    if root is None:
        return None 
    curr = root
    stack = []
    small = []
    while curr is not None:
        stack.append(curr)
        curr = curr.left
        while curr is None and stack:
            node = stack.pop()
            small.append(node.data)
            curr = node.right
    # print(small)
    print(small[k - 1])
tree = None
for i in map(int, input().split()):
    tree = insert(tree, i)
if n >= k:
    smallest(tree, k)
else:
    print(-1)