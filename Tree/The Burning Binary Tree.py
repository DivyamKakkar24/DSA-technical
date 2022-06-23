from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None 


class BurningTree:
    def __init__(self):
        self.root = None 
        self.Q = deque()
    
    def startBurning(self, root, target):
        if root == None:
            return 0

        if root.val == target:
            print(root.val)
            if root.left:
                self.Q.append(root.left)
            if root.right:
                self.Q.append(root.right) 
            return 1
        
        left = self.startBurning(root.left, target)

        if left == 1:
            n = len(self.Q)

            for i in range(n):
                node = self.Q.popleft()
                print(node.val, end = ' ')
                if node.left:
                    self.Q.append(node.left)
                if node.right:
                    self.Q.append(node.right)
            
            print(root.val)
            
            if root.right:
                self.Q.append(root.right)

            return 1 
        
        right = self.startBurning(root.right, target)

        if right == 1:
            n = len(self.Q)

            for i in range(n):
                node = self.Q.popleft()
                print(node.val, end = ' ')
                if node.left:
                    self.Q.append(node.left)
                if node.right:
                    self.Q.append(node.right)
            
            print(root.val)
            
            if root.left:
                self.Q.append(root.left)

            return 1


if __name__ == "__main__":
    tree = BurningTree()
    tree.root = Node(3)
    tree.root.left = Node(5)
    tree.root.right = Node(1)
    tree.root.left.left = Node(6)
    tree.root.left.right = Node(2)
    tree.root.right.left = Node(0)
    tree.root.right.right = Node(8)
    tree.root.left.right.left = Node(7)
    tree.root.left.right.right = Node(4)

    target = 5
    tree.startBurning(tree.root, target)

    while len(tree.Q) > 0:
        n = len(tree.Q)
        for i in range(n):
            node = tree.Q.popleft()
            print(node.val, end = ' ')

            if node.left:
                tree.Q.append(node.left)
            if node.right:
                tree.Q.append(node.right)
        print()




