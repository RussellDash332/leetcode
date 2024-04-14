# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:
    def inorderTraversal(self, root):
        result = []
        def inorder(node):
            if not node: return
            inorder(node.left)
            node.pos = len(result)
            result.append('{}#{}'.format(node.val, node.pos))
            inorder(node.right)
        inorder(root)
        return result

    def postorderTraversal(self, root):
        result = []
        def postorder(node):
            if not node: return
            postorder(node.left)
            postorder(node.right)
            result.append('{}#{}'.format(node.val, node.pos))
        postorder(root)
        return result

    def buildTree(self, inorder, postorder):
        if not inorder: return
        val = postorder[-1]
        idx = inorder.index(val)
        return TreeNode(
            val[0],
            self.buildTree(inorder[:idx], postorder[:idx]),
            self.buildTree(inorder[idx+1:], postorder[idx:-1])
        )

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        inorder, postorder = self.inorderTraversal(root), self.postorderTraversal(root)
        return str(inorder) + '@' + str(postorder)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '[]@[]': return
        def parse(ser):
            v, i = ser[1:-1].split('#') # kill single quotes
            return (int(v), int(i))
        inorder, postorder = list(map(lambda x: list(map(parse, x[1:-1].split(', '))), data.split('@')))
        return self.buildTree(inorder, postorder)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
