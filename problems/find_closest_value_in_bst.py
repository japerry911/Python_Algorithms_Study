class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def findClosestValueInBst(tree: BST, target: int) -> int:
    return _traverse_tree(tree, target, tree.value)


def _traverse_tree(tree: BST, target: int, closest: int) -> int:
    if tree is None:
        return closest

    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value

    if target < tree.value:
        return _traverse_tree(tree.left, target, closest)
    elif target > tree.value:
        return _traverse_tree(tree.right, target, closest)
    else:
        return closest