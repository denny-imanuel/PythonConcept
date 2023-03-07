class MyBinaryTree:

    class Node:

        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self, data):
        self.root = self.Node(data)

    def insert_node(self, node: Node, data):
        if node is not None:
            if data < node.data:
                node.left = self.insert_node(node.left, data)
            if data > node.data:
                node.right = self.insert_node(node.right, data)
            if data == node.data:
                return node
        else:
            return self.Node(data)

    def remove_node(self, node: Node, data):
        if node is not None:
            if data < node.data:
                self.remove_node(node.left, data)
            if data > node.data:
                self.remove_node(node.right,data)
            else:
                node.data = None
                node.left = None
                node.right = None
        return

    def dfs_pre_order(self, node: Node):
        if node is not None:
            print(node.data + "->")
            self.dfs_pre_order(node.left)
            self.dfs_pre_order(node.right)
        return

    def dfs_in_order(self, node: Node):
        if node is not None:
            self.dfs_in_order(node.left)
            print(node.data + "->")
            self.dfs_in_order(node.right)
        return

    def dfs_post_order(self, node: Node):
        if node is not None:
            self.dfs_post_order(node.left)
            self.dfs_post_order(node.right)
            print(node.data + "->")
        return

    def bfs_using_stack(self, node: Node):
        stack = [node]
        while len(stack) is not 0:
            last = stack.pop()
            print(last.data + "->")
            if last.left is not None:
                stack.append(last.left)
            if last.right is not None:
                stack.append(last.right)
        return

    def bfs_using_queue(self, node: Node):
        queue = [node]
        while len(queue) is not 0:
            first = queue.pop(0)
            print(first.data + "->")
            if first.left is not None:
                queue.append(first.left)
            if first.right is not None:
                queue.append(first.right)
        return