class Node:
  def __init__(self, key):
      self.left = None
      self.right = None
      self.val = key


class BinaryTree:
  def __init__(self):
      self.root = None

  def insert(self, root, key):
      if root is None:
          return Node(key)
      else:
          if root.val < key:
              root.right = self.insert(root.right, key)
          else:
              root.left = self.insert(root.left, key)
      return root


  def inorder_traversal(self, root):
      if root:
          self.inorder_traversal(root.left)
          print(root.val, end=' ')
          self.inorder_traversal(root.right)




tree = BinaryTree()
keys = [5, 37, 71, 24, 6, 8,0,0.88,99,0.9,-9]

for key in keys:
  tree.root = tree.insert(tree.root, key)

print("In-order traversal of the binary tree:")
tree.inorder_traversal(tree.root)
