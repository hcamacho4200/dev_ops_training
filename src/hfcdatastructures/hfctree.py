from typing import Any, List


class HFCTreeNode:
    """Node definition for HFCTree
    - keep things simple, create a node and associate it to a parent node
    - a child can have only one parent.
    - its important that we can quickly find a childs parent without searching the entire tree
    - allow for depth 1st traversal
    - Questions:
        - What is the effeciency of searching for a key in this structure?
        - How can this be improved.
        - we are using _root.children = [_parent1, _parent2, _parent3] to assign the children, what must we account for when we do this?
        - What if we wanted to have data with this, how could be improve the structure?
        - What if we needed the keys to be unique?

    """

    def __init__(self, key: str = None):
        self._key = key
        self._children: List[HFCTreeNode] = []
        self._parent = None
        self.data: Any = None

    def add_child(self, child: 'HFCTreeNode'):
        """
        Add a child to a node
        - unmark the existing parent as a parent
        - add the new child
        - set its new parent as self.

        :param child:
        :return:
        """
        _prev_parent = child.parent
        if _prev_parent:
            _prev_parent._children.remove(child)

        _new_parent = self
        _new_parent._children.append(child)
        child.parent = _new_parent

    def change_parent(self, parent):
        """

        :param parent:
        :return:
        """

        if self._parent:
            self._parent._children.remove(self)

        parent._children.append(self)
        self.parent = parent

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, value):
        for _node in self._children:  # type: HFCTreeNode
            _node._parent = None
        self._children = value
        for _node in self._children:  # type: HFCTreeNode
            _node._parent = self

    @property
    def key(self):
        return self._key if self._key else 'Root'

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    def print_tree(self, node=None, level=0):
        """

        :param Node:
        :return:
        """
        if not node:
            print()
            node = self

        print('  ' * level, node.key)
        for _child in node._children:
            self.print_tree(node=_child, level=level+1)

    def __repr__(self):
        return f'[HFCTreeNode key={self.key}, parent={self._parent.key}]'
