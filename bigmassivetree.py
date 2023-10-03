class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root) -> None:
        self.root = Node(root)

    def print_traversal(self, traversal_type):

        if traversal_type == "preorder":
            return self.preorder(self.root, "")
        elif traversal_type == "preorder stack":
            return self.preorder_with_stack(self.root)

        elif traversal_type == "inorder":
            return self.inorder(self.root, "")
        elif traversal_type == "inorder stack":
            return self.inorder_with_stack(self.root)

        elif traversal_type == "postorder":
            return self.postorder(self.root, "")
        elif traversal_type == "postorder stack":
            return self.postorder_with_stack(self.root)

        elif traversal_type == "leaves":
            return self.leaves(self.root, "")

    # define some traversal functions
    def preorder(self, node, traversal):
        if node:
            traversal += f"{node.value},"
            traversal = self.preorder(node.left, traversal)
            traversal = self.preorder(node.right, traversal)
        return traversal

    def preorder_with_stack(self, root):
        cur = root
        stack = []
        traversal = ""

        while cur or stack:
            if cur:
                traversal += f"{cur.value},"
                stack.append(cur.right)
                cur = cur.left
            else:
                cur = stack.pop()

        return traversal

    def inorder(self, node, traversal):
        if node:
            traversal = self.inorder(node.left, traversal)
            traversal += f"{node.value},"
            traversal = self.inorder(node.right, traversal)
        return traversal

    def inorder_with_stack(self, root):
        cur = root
        stack = []
        traversal = ""

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                traversal += f"{cur.value},"
                cur = cur.right

        return traversal

    def postorder(self, node, traversal):
        if node:
            traversal = self.postorder(node.left, traversal)
            traversal = self.postorder(node.right, traversal)
            traversal += f"{node.value},"
        return traversal

    def postorder_with_stack(self, root):
        cur = root
        stack = []
        traversal = []

        while cur or stack:
            if cur:
                traversal += f"{cur.value}"
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop()
                cur = cur.left

        traversal.reverse()
        return str(traversal).replace('[', '').replace(']', '').replace("'", '').replace(' ', '') + ','

    def invert(self):
        return self.invert_tree(self.root)

    # Invert Function
    def invert_tree(self, node):
        if node:
            left = self.invert_tree(node.left)
            right = self.invert_tree(node.right)
            node.left = right
            node.right = left
        return node

    # print all leaves
    def leaves(self, node, traversal):
        if node.left is None and node.right is None:
            traversal += f"{node.value},"
            return traversal

        traversal = self.leaves(node.left, traversal)
        traversal = self.leaves(node.right, traversal)

        return traversal

    def depth(self):
        return self.find_depth(self.root, 0) - 1

    def find_depth(self, node, depth):
        if node:
            depth_left = self.find_depth(node.left, depth + 1)
            depth_right = self.find_depth(node.right, depth + 1)
            depth = max(depth_left, depth_right)

        return depth

    def min_depth(self, root):
        # perform DFS and keep track of a count?
        def postorder(node, depth):
            nonlocal result
            if not node:
                if depth < result or result == 0:
                    result = depth
                return

            postorder(node.left, depth + 1)
            postorder(node.right, depth + 1)

        result = 0
        postorder(root, 1)
        return result


if __name__ == '__main__':
    #         1
    #       /   \
    #     2       3
    #    / \
    #   4   5

    #         1
    #       /   \
    #     3       2
    #            / \
    #           5   4

    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    print(tree.print_traversal("preorder"))
    print(tree.print_traversal("preorder stack"))
    print(tree.print_traversal("inorder"))
    print(tree.print_traversal("inorder stack"))
    print(tree.print_traversal("postorder"))
    print(tree.print_traversal("postorder stack"))
    print(tree.print_traversal("leaves"))
    print(tree.min_depth(tree.root))
    tree.invert()
    print(tree.print_traversal("preorder"))
    print(tree.depth())
    tree.root.right.right.right = Node(6)
    tree.root.right.right.right.left = Node(7)
    tree.root.right.right.right.left.left = Node(8)
    print(tree.print_traversal("preorder"))
    print(tree.depth())
