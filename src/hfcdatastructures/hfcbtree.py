
class TreeNode(object):
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        self.height = 1

    def __repr__(self):
        return f'TreeNode {self.value}'


class HFCBTree:
    """

    """

    def __init__(self, value=None):
        self._root = None
        pass

    def insert(self, value, root=None):
        """

        :param value:
        :param node:
        :return:
        """
        # handle root case creation

        if not root:
            return TreeNode(value)

        if value < root.value:
            root.left = self.insert(value, root=root.left)
        else:
            root.right = self.insert(value, root=root.right)

        return root

    def print2DTree(self, root, space=0, LEVEL_SPACE=5):
        """

        :param root:
        :param space:
        :param LEVEL_SPACE:
        :return:
        """
        if not root:
            return

        space += LEVEL_SPACE

        self.print2DTree(root.right, space)
        # print() # neighbor space
        for i in range(LEVEL_SPACE, space):
            print(end=" ")

        print("|" + str(root.value) + "|<")
        self.print2DTree(root.left, space)
