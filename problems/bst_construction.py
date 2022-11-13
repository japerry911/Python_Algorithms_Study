# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value: int):
        tree = self

        while True:
            if value >= tree.value:
                if tree.right is None:
                    tree.right = BST(value=value)
                    break

                tree = tree.right
            else:
                if tree.left is None:
                    tree.left = BST(value=value)
                    break

                tree = tree.left
        
        return self

    def contains(self, value: int) -> bool:
        tree = self

        while tree is not None:
            if value == tree.value:
                return True
            elif value > tree.value:
                tree = tree.right
            else:
                tree = tree.left

        return False

    def remove(self, value: int, parent_node = None):
        tree = self

        while tree is not None:
            if value < tree.value:
                parent_node = tree
                tree = tree.left
            elif value > tree.value:
                parent_node = tree
                tree = tree.right
            else:
                if tree.left is not None and tree.right is not None:
                    tree.value = tree.right.get_min_value()
                    tree.right.remove(tree.value, tree)
                elif parent_node is None:
                    if tree.left is not None:
                        tree.value = tree.left.value
                        tree.right = tree.left.right
                        tree.left = tree.left.left
                    elif tree.right is not None:
                        tree.value = tree.right.value
                        tree.left = tree.right.left
                        tree.right = tree.right.right
                    else:
                        # single-node tree, do nothing
                        pass
                elif parent_node.left == tree:
                    parent_node.left = tree.left if tree.left is not None else tree.right
                elif parent_node.right == tree:
                    parent_node.right = tree.left if tree.left is not None else tree.right

                break
            
        return self

    def get_min_value(self) -> int:
        tree = self

        while tree.left is not None:
            tree = tree.left

        return tree.value
