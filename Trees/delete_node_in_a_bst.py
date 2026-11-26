# Delete Node in a BST (LeetCode 450) - Trees
# Approach: Recursion. Go right if key is bigger, left if smaller, and
#           re-attach the result. When found:
#             - no left child  -> replace it with its right child
#             - no right child -> replace it with its left child
#             - both children  -> copy the smallest value of the right subtree
#               into this node, then delete that smallest node from the right
#               subtree (it has no left child, so that delete is easy).
#           An empty spot returns None (returning False attached a bool to the
#           tree and broke LeetCode's printer).
# Time: O(h)  |  Space: O(h) for the recursion stack (h = tree height)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def minValueNode(root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr
        
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            #Found the node to be removed
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # Both children present replace with min Node
                minNode = minValueNode(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
        return root
