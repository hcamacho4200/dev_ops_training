from src.hfcdatastructures.hfcavltree import AVL_Tree


def test_hfcavltree():
    """

    :return:
    """

    myTree = AVL_Tree()
    root = None



    # root = myTree.insert(root, 30)
    # root = myTree.insert(root, 40)
    # root = myTree.insert(root, 20)
    # print()
    # myTree.print2DTree(root)

    root = myTree.insert(root, 10)
    root = myTree.insert(root, 20)
    root = myTree.insert(root, 30)
    root = myTree.insert(root, 40)
    root = myTree.insert(root, 50)
    root = myTree.insert(root, 25)
    root = myTree.insert(root, 26)
    root = myTree.insert(root, 27)
    root = myTree.insert(root, 28)
    root = myTree.insert(root, 29)
    root = myTree.insert(root, 31)
    root = myTree.insert(root, 32)
    myTree.print2DTree(root)
