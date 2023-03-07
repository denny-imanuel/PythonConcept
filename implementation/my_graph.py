class MyGraph:

    def __init__(self):
        self.graph = {}

    def add_vertex(self, val):
        if not self.graph.__contains__(val):
            self.graph[val] = None

    def remove_vertex(self, val):
        if self.graph.__contains__(val):
            del self.graph[val]

    def add_edges(self, val1, val2):
        if not self.graph.__contains__(val1) and self.graph.__contains__(val2):
            self.graph[val1].append([val2])

    def remove_edges(self, val1, val2):
        if self.graph.__contains__(val1) and self.graph.__contains__(val2):
            self.graph[val1].remove(val2)

    def print_graph(self):
        for key in self.graph:
            for val in self.graph[key]:
                print('graph:', key, '->', val)

    def dfs_using_stack(self, start):
        visited = set()
        stack = [start]
        while stack:
            # get first in stack and mark as visited
            first = stack.pop()
            if first not in visited:
                visited.add(first)
                # get adj vertex and insert it to stack
                neighbors = self.graph[first].values
                # add stack with adj vertex except the one that has been visited
                stack.extend(neighbors-visited)
                print('dfs traverse:', visited)
        return visited

    def bfs_using_queue(self, start):
        visited = set()
        queue = [start]
        while queue:
            # get the last in queue and mark as visited
            last = queue.pop(0)
            if last not in visited:
                visited.add(last)
                # get adj vertex and insert it to queue
                neighbors = self.graph[last].values
                # add queue with adj vertex except the one that has been visited
                queue.extend(neighbors - visited)
                print('bfs traverse:', visited)
        return visited


if __name__ == '__main__':
    graph = MyGraph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 1)
    graph.print_graph()
    graph.dfs_using_stack(1)
    graph.bfs_using_queue(1)