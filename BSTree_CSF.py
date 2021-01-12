# @Rexhino_Kovaci
# balanced search tree is balanced if the difference between the height of the right and left subtrees is 1 or 0.
# in this implementation I've imported bst from the binarytree.py libray

from binarytree import bst

root = bst()
print('BST of any height : \n',
      root)

root2 = bst(height=3)
print('BST of given height : \n',
      root2)

root3 = bst(height=3,
            is_perfect=True)
print('Perfect BST of given height : \n',
      root3)