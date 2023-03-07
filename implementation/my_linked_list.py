class MyLinkedList:

    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self, data):
        self.head = MyLinkedList(data).Node(data)
        return

    def traverse_node(self, node: Node):
        if node.next is not None:
            print(node.data)
            self.traverse_node(node.next)
        return

    def insert_node(self, node: Node, data):
        new_node = MyLinkedList(data).Node(data)
        if node.next is not None:
            self.insert_node(node.next, data)
        else:
            node.next = new_node
        return

    def remove_node(self, node: Node, data):
        prev_node = node
        if node.next is not None:
            if data == node.data:
                prev_node.next = node.next
            else:
                self.remove_node(node.next, data)
        return
