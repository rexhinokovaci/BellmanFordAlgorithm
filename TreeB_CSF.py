# @Rexhino_Kovaci
# This is an extra exercises that I challenged myself with on Google Kickstart 2020 during the online sessions
# This algorithm takes user input and compare the left and right subtree
# this would allow us to maintain a sorted list of numbers
# this program would check if the tree is balanced between the height of right and left subtree is 1 or 0



class Tree(object):
    from binarytree import Node
    root = Node(int(input("Enter Root: ")))
    root.left = Node(int(input("Enter Left Subtree: ")))
    root.right = Node(int(input("Enter Right Subtree: ")))


    print('Binary tree :', root)


    print('List of nodes :', list(root))

    print('Inorder of nodes :', root.inorder)


    print('Size of tree :', root.size)
    print('Height of tree :', root.height)

    print('Properties of tree : \n', root.properties)


#     This would print all the properties of the nodes list, order, size, height, properties of our Balanced Search Tree



