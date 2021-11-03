# Course: CS261 - Data Structures
# Author: Richard Frank
# Assignment: 6 - graphs
# Description: This program contains all functionality for the directed graph portion of the assignment.

import heapq
from collections import deque

class DirectedGraph:
    """
    Class to implement directed weighted graph
    - duplicate edges not allowed
    - loops not allowed
    - only positive edge weights
    - vertex names are integers
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency matrix
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.v_count = 0
        self.adj_matrix = []

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if self.v_count == 0:
            return 'EMPTY GRAPH\n'
        out = '   |'
        out += ' '.join(['{:2}'.format(i) for i in range(self.v_count)]) + '\n'
        out += '-' * (self.v_count * 3 + 3) + '\n'
        for i in range(self.v_count):
            row = self.adj_matrix[i]
            out += '{:2} |'.format(i)
            out += ' '.join(['{:2}'.format(w) for w in row]) + '\n'
        out = f"GRAPH ({self.v_count} vertices):\n{out}"
        return out

    # ------------------------------------------------------------------ #

    def add_vertex(self) -> int:
        """
        This method adds a new vertex to the graph.
        """
        self.v_count += 1
        row = [0] * self.v_count
        self.adj_matrix.append(row)

        for value in range(self.v_count-1):
            self.adj_matrix[value].append(0)

        return self.v_count

    def add_edge(self, src: int, dst: int, weight=1) -> None:
        """
        This method adds a new edge to the graph, connecting two vertices with provided indices.
        """
        if src == dst or src >= self.v_count or src < 0 or dst < 0 or dst >= self.v_count or weight < 0:
            return
        self.adj_matrix[src][dst] = weight

    def remove_edge(self, src: int, dst: int) -> None:
        """
        This method removes an edge between two vertices with provided indices.
        """
        if src == dst or src >= self.v_count or src < 0 or dst < 0 or dst >= self.v_count:
            return
        self.adj_matrix[src][dst] = 0

    def get_vertices(self) -> []:
        """
        This method returns a list of vertices of the graph.
        """
        ret_list = []
        for i in range(self.v_count):
            ret_list.append(i)
        return ret_list

    def get_edges(self) -> []:
        """
        This method returns a list of edges in the graph.
        """
        ret_list = []
        for i in range(self.v_count):
            for j in range(self.v_count):
                if self.adj_matrix[i][j] != 0:
                    ret_list.append((i, j, self.adj_matrix[i][j]))
        return ret_list

    def is_valid_path(self, path: []) -> bool:
        """
        This method takes a list of vertex indices and returns True if the sequence of vertices
        represents a valid path in the graph
        """
        for i in range(len(path)-1):
            if self.adj_matrix[path[i]][path[i+1]] == 0:
                return False
        return True

    def dfs(self, v_start, v_end=None) -> []:
        """
        This method performs a depth-first search (DFS) in the graph and returns a list of vertices
        visited during the search, in the order they were visited.
        """
        if v_start not in self.get_vertices():
            return []
        elif v_start == v_end:
            return [v_start]

        visited = []
        stack = deque()
        stack.append(v_start)
        self.dfs_helper(visited, v_start, v_end)
        return visited

    def dfs_helper(self, visited, value, v_end):
        if value not in visited:
            visited.append(value)
            reachable = []
            for i in range(self.v_count):
                if self.adj_matrix[value][i] != 0 and i not in visited:
                    reachable.append(i)
            reachable.sort()
            for neighbour in reachable:
                if neighbour == v_end:
                    if v_end not in visited:
                        visited.append(v_end)
                    return
                else:
                    if v_end not in visited:
                        self.dfs_helper(visited, neighbour, v_end)


    #     vertices = self.get_vertices()
    #     tracker = {}
    #     for vertex in vertices:
    #         tracker[vertex] = False
    #     visited = []
    #     self.dfs_helper(v_start, tracker, visited)
    #     return visited
    #
    # def dfs_helper(self, node, tracker, visited):
    #
    #
    #     visited.append(node)
    #     tracker[node] = True
    #
    #     for i in range(self.v_count):
    #         if self.adj_matrix[node][i] != 0 and (not tracker[i]):
    #             self.dfs(i, tracker, visited)
    #     return visited
        # if v_start > self.v_count or v_start < 0:
        #     return []
        # visited = []
        # stack = deque()
        # stack.append(v_start)
        # reachable = []
        # while stack:
        #     if len(reachable) > 0:
        #         vertex = min(reachable)
        #         stack.remove(vertex)
        #     elif len(reachable) == 0:
        #         s = sorted(stack)
        #         vertex = s[0]
        #         stack.remove(vertex)
        #     else:
        #         vertex = stack.popleft()
        #     if vertex not in visited:
        #         visited += [vertex]
        #     reachable = []
        #     for i in range(self.v_count):
        #         if self.adj_matrix[vertex][i] != 0 and i not in visited:
        #             stack.append(i)
        #             reachable.append(i)
        #     if v_end in visited:
        #         return visited
        # return visited


    def bfs(self, v_start, v_end=None) -> []:
        """
        This method performs a breadth-first search (BFS) in the graph and returns a list of vertices
        visited during the search, in the order they were visited.
        """
        if v_start > self.v_count or v_start < 0:
            return []

        visited = []
        queue = []

        visited.append(v_start)
        queue.append(v_start)
        if v_start == v_end:
            return visited

        while queue:
            vertex = queue.pop(0)
            reachable = []
            for i in range(self.v_count):
                if self.adj_matrix[vertex][i] != 0:
                    reachable += [i]
            for item in reachable:
                if item == v_end:
                    visited.append(item)
                    return visited
                if item not in visited:
                    visited.append(item)
                    queue.append(item)
        return visited

    def has_cycle(self):
        """
        This method returns True if there is at least one cycle in the graph. If the graph is acyclic,
        the method returns False.
        """
        vertices = self.get_vertices()
        visited = {}
        for vertex in vertices:
            visited[vertex] = False

        stack = {}
        for vertex in vertices:
            stack[vertex] = False

        for node in range(self.v_count):
            if visited[node] == False:
                if self.cycle_helper(node, visited, stack) == True:
                    return True
        return False


    def cycle_helper(self, value, visited, stack):
        visited[value] = True
        stack[value] = True
        reachable = []
        for i in range(self.v_count):
            if self.adj_matrix[value][i] != 0:
                reachable += [i]
        for j in reachable:
            if visited[j] == False:
                if self.cycle_helper(j, visited, stack) == True:
                    return True
            elif stack[j] == True:
                return True
        stack[value] = False
        return False

    def dijkstra(self, src: int) -> []:
        """
        This method implements the Dijkstra algorithm to compute the length of the shortest path
        from a given vertex to all other vertices in the graph.
        """
        vertices = self.get_vertices()
        node_distance = {}
        for vertex in vertices:
            node_distance[vertex] = float('inf')

        node_distance[src] = 0

        visited = {}
        for vertex in vertices:
            visited[vertex] = False

        for val in range(self.v_count):
            min = 0
            for key in node_distance.keys():
                if node_distance[key] > min:
                    min = node_distance[key]
                    min_index = key

            for i in range(self.v_count):
                if node_distance[i] < min and visited[i] == False:
                    min = node_distance[i]
                    min_index = i

            visited[min_index] = True

            for j in range(self.v_count):
                if self.adj_matrix[min_index][j] > 0 and visited[j] == False and node_distance[j] > node_distance[min_index] + self.adj_matrix[min_index][j]:
                    node_distance[j] = node_distance[min_index] + self.adj_matrix[min_index][j]

        ret_list = []
        for key in node_distance.keys():
            ret_list += [node_distance[key]]

        return ret_list


if __name__ == '__main__':

    print("\nPDF - method add_vertex() / add_edge example 1")
    # print("----------------------------------------------")
    # g = DirectedGraph()
    # print(g)
    # for _ in range(12):
    #     g.add_vertex()
    # print(g)
    # #
    # # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    # #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # # for src, dst, weight in edges:
    # #     g.add_edge(src, dst, weight)
    # g.add_edge(7, 12, 16)
    # print(g)


    # print("\nPDF - method get_edges() example 1")
    # print("----------------------------------")
    # g = DirectedGraph()
    # print(g.get_edges(), g.get_vertices(), sep='\n')
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    # print(g.get_edges(), g.get_vertices(), sep='\n')
    # edges = [(0, 6, 14), (0, 7, 10), (0, 8, 20), (2, 8, 2), (3, 8, 1), (4, 3, 4), (6, 1, 13), (7, 0, 7), (7, 10, 10), (7, 12, 20), (8, 0, 5), (11, 3, 14), (11, 6, 1), (12, 9, 15)]
    # g = DirectedGraph(edges)
    # print(g)
    # print(g.dfs(0))

    # print("\nPDF - method is_valid_path() example 1")
    # print("--------------------------------------")
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    # test_cases = [[0, 1, 4, 3], [1, 3, 2, 1], [0, 4], [4, 0], [], [2]]
    # for path in test_cases:
    #     print(path, g.is_valid_path(path))
    #
    # #
    # print("\nPDF - method dfs() and bfs() example 1")
    # print("--------------------------------------")
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    # for start in range(5):
    #     print(f'{start} DFS:{g.dfs(start)} BFS:{g.bfs(start)}')
    #
    # #
    # print("\nPDF - method has_cycle() example 1")
    # print("----------------------------------")
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    #
    # edges_to_remove = [(3, 1), (4, 0), (3, 2)]
    # for src, dst in edges_to_remove:
    #     g.remove_edge(src, dst)
    #     print(g.get_edges(), g.has_cycle(), sep='\n')
    #
    # edges_to_add = [(4, 3), (2, 3), (1, 3), (4, 0)]
    # for src, dst in edges_to_add:
    #     g.add_edge(src, dst)
    #     print(g.get_edges(), g.has_cycle(), sep='\n')
    # print('\n', g)

    #
    # print("\nPDF - dijkstra() example 1")
    # print("--------------------------")
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    # for i in range(5):
    #     print(f'DIJKSTRA {i} {g.dijkstra(i)}')
    # g.remove_edge(4, 3)
    # print('\n', g)
    # for i in range(5):
    #     print(f'DIJKSTRA {i} {g.dijkstra(i)}')
