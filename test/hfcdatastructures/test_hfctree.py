from src.hfcdatastructures.hfctree import HFCTreeNode


def test_hfctree():
    """

    :return:
    """

    # _root = HFCTreeNode()
    # _root.print_tree()
    #
    # _parent1 = HFCTreeNode(key='Parent1')
    # _parent2 = HFCTreeNode(key='Parent2')
    # _parent3 = HFCTreeNode(key='Parent3')
    # _root.children = [_parent1, _parent2, _parent3]
    # _root.print_tree()
    #
    # _parent1_child1 = HFCTreeNode('p1c1')
    # _parent1_child2 = HFCTreeNode('p1c2')
    # _parent1_child3 = HFCTreeNode('p1c3')
    # _parent1.children = [_parent1_child1, _parent1_child2, _parent1_child3]
    # _root.print_tree()
    #
    # _parent2_child1 = HFCTreeNode('p2c1')
    # _parent2.children = [_parent2_child1]
    # _root.print_tree()
    #
    # _parent3_child1 = HFCTreeNode('p3c1')
    # _parent3_child2 = HFCTreeNode('p3c2')
    # _parent3_child3 = HFCTreeNode('p3c3')
    # _parent3_child4 = HFCTreeNode('p3c4')
    # _parent3_child5 = HFCTreeNode('p3c5')
    # _parent3.children = [_parent3_child1, _parent3_child2, _parent3_child3, _parent3_child4, _parent3_child5]
    # _root.print_tree()
    #
    # _parent3_child5.change_parent(_root)
    # _root.print_tree()
    #
    # _parent3_child5.change_parent(_parent2_child1)
    # _root.print_tree()

    # different approach
    _root = HFCTreeNode()
    _root.print_tree()
    #
    _parent1 = HFCTreeNode(key='Parent1')
    _root.add_child(_parent1)
    _parent2 = HFCTreeNode(key='Parent2')
    _root.add_child(_parent2)
    _root.print_tree()
    _parent1.add_child(_parent2)
    _root.print_tree()

    print(_root.key, _root._key)




    assert False

