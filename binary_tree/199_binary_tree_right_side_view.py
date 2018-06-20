class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left = b
a.right = c
b.left = d
b.right = e

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []


        stack = [root] if root else []

        while stack:
            result.append(stack[-1].val)
            stack = [child for parent in stack for child in [parent.left, parent.right] if child]

        return result

    def rightSideView2(self, root):

        result = []
        stack = []

        if root:
            stack.append(root)

        def run_stack(stack):
            new_stack = []
            if stack:
                a = stack.pop(0)
                print(a.val)
                result.append(a.val)
                if a.right:
                    new_stack.append(a.right)
                if a.left:
                    new_stack.append(a.left)
                while stack:
                    b = stack.pop(0)
                    if b.right:
                        new_stack.append(b.right)
                    if b.left:
                        new_stack.append(b.left)
                if not stack:
                    stack = new_stack
                    run_stack(stack)

        run_stack(stack)
        return result


        ## print Binary tree breath-first
        # stack = list()
        # def print_breath_first(node):
        #     stack.append(node)
        #
        #     while stack:
        #         a = stack.pop(0)
        #         print(a.val)
        #         if a.left:
        #             stack.append(a.left)
        #         if a.right:
        #             stack.append(a.right)
        # print_breath_first(root)

print(Solution().rightSideView(a)
)
# def preorder_print(node, layer):
#     if not node:
#         return
#
#     for i in range(layer):
#         print("---")
#
#     print("{}\n".format(node.val))
#     preorder_print(node.left, layer+1)
#     preorder_print(node.right, layer+1)
#
# preorder_print(a, 0)
