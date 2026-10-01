class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    new = TreeNode(data)
    if root is None:
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
def reverse_inorder(root, total):
    if root is None:
        return None 
    reverse_inorder(root.right, total)
    root.data += total[0]
    total[0] = root.data
    print(root.data, end=" ")
    reverse_inorder(root.left, total)

n = int(input())
tree = None
for i in map(int, input().split()):
    tree = insert(tree, i)
reverse_inorder(tree, [0])