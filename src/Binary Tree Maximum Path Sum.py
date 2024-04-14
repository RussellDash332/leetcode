class Solution(object):
    memo = {}

    def maxPathSum(self, root, memo=memo):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root in memo:
            return memo[root]

        def helper_with_root(root, cr=False, memo=memo):
            if (root, cr) in memo:
                return memo[(root, cr)]
            if not root:
                return -float('inf')
            sl = helper_with_root(root.left)
            sr = helper_with_root(root.right)
            v = root.val
            memo[(root, cr)] = max(v, v + sl, v + sr, v + sl + sr if cr else -float('inf'))
            return memo[(root, cr)]

        def helper_without_root(root):
            if not root:
                return -float('inf')
            sl = self.maxPathSum(root.left)
            sr = self.maxPathSum(root.right)
            return max(sl, sr)

        memo[root] = max(helper_with_root(root, True), helper_without_root(root))
        return memo[root]
