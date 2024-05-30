import unittest
from tree import Tree


class TestTree(unittest.TestCase):
    
    def test_tree1(self):
        tree = Tree()
        tree.add(3)
        tree.add(4)
        tree.add(0)
        tree.add(8)
        tree.add(2)
        
        node = tree.getRoot()
        node = node.right
        assert tree._find(4, tree.getRoot()) == node
        
    def test_tree2(self):
        tree = Tree()
        tree.add(3)
        tree.add(4)
        tree.add(0)
        tree.add(8)
        tree.add(2)
        
        node = tree.getRoot()
        node = node.right
        assert tree._find(0, node) == None
        
        
if __name__ == '__main__':
    unittest.main()