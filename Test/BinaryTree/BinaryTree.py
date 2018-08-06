from tkinter import *
class BinaryTreeNode:
    count = 0
    def __init__(self, value):
        self.Left = None
        self.Right = None
        self.node = value
        BinaryTreeNode.count += 1
    def compareTo(self, value):
        if self.node > value:
            return -1
        elif self.node < value:
            return 1
        else:
            return 0

class BinaryTree:
    head = ''
    def __init__(self):
        pass
    def add(self, value):
        if BinaryTree.head:
            self.addTo(BinaryTree.head, value)
        else:
            BinaryTree.head = BinaryTreeNode(value)

    def addTo(self, node, value):
        if node.compareTo(value) < 0:
            if node.Left:
                self.addTo(node.Left, value)
            else:
                node.Left = BinaryTreeNode(value)
        else:
            if node.Right:
                self.addTo(node.Right, value)
            else:
                node.Right = BinaryTreeNode(value)

    def contains(self, value):
        self.__findWithParent(value)

    def __findWithParent(self, value):
        current = BinaryTree.head

class printTree(Frame):
    x_l = 50
    y_l = 30
    def __init__(self, tree=None, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.canvas = Canvas(width=526, height=600, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)
        start_x = 250
        start_y = 10
        self.createRect(tree.head, start_x, start_y)
    def createRect(self, node, x, y):
        if node:
            self.canvas.create_rectangle(x,y, x+printTree.x_l,y+printTree.y_l, width=2, fill='white')
            self.canvas.create_text((x+22, y+15), text= node.node)
            self.createRect(node.Left, x-30, y+40)
            self.createRect(node.Right, x + 30, y + 40)

# def rectForNode(node):
#     if node:
#         canvas.create_rectangle(250, 10, 300, 40, width=2, fill='blue')

if __name__ == "__main__":
    btr = BinaryTree()
    btr.add(5)
    btr.add(4)
    btr.add(6)
    btr.add(5)
    btr.add(6)
    btr.add(7)
    btr.add(3)
    btr.add(2)
    btr.add(8)
    btr.add(1)
    btr.add(9)
    print(btr.head.count)
    printTree(btr).mainloop()