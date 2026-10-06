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
        if data == cur.data:
            return root
        elif data < cur.data:
            if cur.left is None:
                cur.left = TreeNode(data)
                return root
            cur = cur.left
        else:
            if cur.right is None:
                cur.right = TreeNode(data)
                return root
            cur = cur.right

def dfs(root):
    if root is None:
        return None 
    stack = [(root, "new")]
    heights = {}
    best = 0
    while stack:
        node, state = stack.pop()
        if state == "new":
            stack.append((node, "ready"))
            if node.right:
                stack.append((node.right, "new"))
            if node.left:
                stack.append((node.left, "new"))
        else:
            leftH = heights.get(node.left, 0)
            rightH = heights.get(node.right, 0)
            heights[node] = 1 + max(leftH, rightH)
            best = max(best, leftH + rightH + 1)
    return best 
n = int(input())
tree = None 
for i in map(int, input().split()):
    tree = insert(tree, i)
print(dfs(tree))

# 2
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def dfs(root):
    if root is None:
        return 0
    depth = 0
    stack = [(root, "new")]
    heights = {}
    best = 0
    while stack:
        node, state = stack.pop()
        if state == "new":
            stack.append((node, "ready"))
            if node.right:
                stack.append((node.right, "new"))
            if node.left:
                stack.append((node.left, "new"))
        else:
            leftH = heights.get(node.left, 0)
            rightH = heights.get(node.right, 0)
            heights[node] = 1 + max(leftH, rightH)
            best = max(leftH + rightH + 1, best)
    return best

def build_fast(raw_vals):
    seen = set()
    vals = []
    for v in raw_vals:
        if v not in seen:
            seen.add(v)
            vals.append(v)
    n = len(vals)
    if n == 0:
        return None

    sorted_order = sorted(range(n), key=lambda i: vals[i])
    rank = [0] * n
    for pos, i in enumerate(sorted_order):
        rank[i] = pos

    prev = [p - 1 if p > 0 else None for p in range(n)]
    nxt  = [p + 1 if p < n - 1 else None for p in range(n)]

    parent_idx = [None] * n
    is_left = [None] * n

    for i in range(n - 1, 0, -1):
        r = rank[i]
        L = prev[r]
        R = nxt[r]

        if L is not None and (R is None or sorted_order[L] > sorted_order[R]):
            parent_idx[i] = sorted_order[L]
            is_left[i] = False
        else:
            parent_idx[i] = sorted_order[R]
            is_left[i] = True

        if L is not None:
            nxt[L] = R
        if R is not None:
            prev[R] = L

    nodes = [TreeNode(v) for v in vals]
    for i in range(1, n):
        p = parent_idx[i]
        if is_left[i]:
            nodes[p].left = nodes[i]
        else:
            nodes[p].right = nodes[i]
    return nodes[0]

n = int(input())
raw = list(map(int, input().split()))
tree = build_fast(raw)
print(dfs(tree))