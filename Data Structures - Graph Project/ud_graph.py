# Course: CS 261 - Data Structures
# Author: Richard Frank
# Assignment: 6 - Graphs
# Description: This program contains all functionality required for an undirected graph.

import heapq
from collections import deque


class UndirectedGraph:
    """
    Class to implement undirected graph
    - duplicate edges not allowed
    - loops not allowed
    - no edge weights
    - vertex names are strings
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.adj_list = dict()

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            for u, v in start_edges:
                self.add_edge(u, v)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = [f'{v}: {self.adj_list[v]}' for v in self.adj_list]
        out = '\n  '.join(out)
        if len(out) < 70:
            out = out.replace('\n  ', ', ')
            return f'GRAPH: {{{out}}}'
        return f'GRAPH: {{\n  {out}}}'

    # ------------------------------------------------------------------ #

    def add_vertex(self, v: str) -> None:
        """
        Add new vertex to the graph
        """
        if len(self.adj_list) == 0:
            self.adj_list[v] = []
        if v not in self.adj_list.keys():
            self.adj_list[v] = []
        else:
            return
        
    def add_edge(self, u: str, v: str) -> None:
        """
        Add edge to the graph
        """
        if u == v:
            return
        else:
            self.add_vertex(u)
            self.add_vertex(v)

            u_list = self.adj_list[u]
            if v not in u_list:
                u_list += v
            v_list = self.adj_list[v]
            if u not in v_list:
                v_list += u
        

    def remove_edge(self, v: str, u: str) -> None:
        """
        Remove edge from the graph
        """
        if (v or u) not in self.adj_list.keys():
            return
        else:
            v_list = self.adj_list[v]
            if u not in v_list:
                return
            u_list = self.adj_list[u]
            if v not in u_list:
                return
            else:
                v_list.remove(u)
                u_list.remove(v)


    def remove_vertex(self, v: str) -> None:
        """
        Remove vertex and all connected edges
        """
        if v not in self.adj_list.keys():
            return
        else:
            del self.adj_list[v]
            for key in self.adj_list.keys():
                if v in self.adj_list[key]:
                    self.adj_list[key].remove(v)

    def get_vertices(self) -> []:
        """
        Return list of vertices in the graph (any order)
        """
        ret_list = []
        for key in self.adj_list.keys():
            ret_list += key
        return ret_list
       

    def get_edges(self) -> []:
        """
        Return list of edges in the graph (any order)
        """
        edge_list = []
        for key in self.adj_list.keys():
            for i in range(len(self.adj_list[key])):
                new_tuple = (key, self.adj_list[key][i])
                test_tuple = (self.adj_list[key][i], key)
                if new_tuple in edge_list or test_tuple in edge_list:
                    continue
                else:
                    edge_list.append(new_tuple)
        return edge_list
        

    def is_valid_path(self, path: []) -> bool:
        """
        Return true if provided path is valid, False otherwise
        """
        if len(path) == 0:
            return True
        else:
            for i in range(len(path)):
                if path[i] not in self.adj_list.keys():
                    return False
            i = 0
            while i < (len(path)-1):
                v1 = path[i]
                v2 = path[i+1]
                if v2 not in self.adj_list[v1]:
                    return False
                else:
                    i += 1
            return True

    def dfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during DFS search
        Vertices are picked in alphabetical order
        """
        if v_start not in self.adj_list:
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
            reachable = self.adj_list[value]
            reachable.sort()
            for neighbour in reachable:
                if neighbour == v_end:
                    if v_end not in visited:
                        visited.append(v_end)
                    return
                else:
                    if v_end not in visited:
                        self.dfs_helper(visited, neighbour, v_end)



    def bfs(self, v_start, v_end=None) -> []:
        """
        Return list of vertices visited during BFS search
        Vertices are picked in alphabetical order
        """
        visited = []
        queue = []
        if v_start not in self.adj_list:
            return []
        visited.append(v_start)
        queue.append(v_start)
        if v_start == v_end:
            return visited

        if v_start not in self.adj_list:
            return []

        while queue:
            s = queue.pop(0)
            reachable = self.adj_list[s]
            reachable.sort()
            for neighbour in reachable:
                if neighbour == v_end:
                    visited.append(neighbour)
                    return visited
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return visited

    def count_connected_components(self):
        """
        Return number of connected components in the graph
        """
        vertices = self.get_vertices()
        tracker = {}
        for vertex in vertices:
            tracker[vertex] = False
        count = 0
        for val in tracker:
            if tracker[val] is False:
                ret_list = self.dfs(val)
                for item in ret_list:
                    tracker[item] = True
                count += 1
        return count

    def has_cycle(self):
        """
        Return True if graph contains a cycle, False otherwise
        """
        vertices = self.get_vertices()
        tracker = {}
        for vertex in vertices:
            tracker[vertex] = False
        for val in tracker:
            if tracker[val] == False:
                if self.cycle_helper(val, tracker, -1):
                    return True
        return False

    def cycle_helper(self, value, tracker, parent):
        tracker[value] = True
        reachable = self.adj_list[value]
        for i in reachable:
            if tracker[i] == False:
                if self.cycle_helper(i, tracker, value):
                    return True
            elif parent != i:
                return True
        return False

   


if __name__ == '__main__':
    #
    # print("\nPDF - method add_vertex() / add_edge example 1")
    # print("----------------------------------------------")
    g = UndirectedGraph()
    print(g)

    for v in 'HKFE':
        g.add_vertex(v)
    print(g)

    g.add_edge("H","K")
    g.add_edge("E","F")
    g.add_edge("G","G")
    print(g)
    #
    # g.add_vertex('A')
    # print(g)
    #
    # for u, v in ['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE', ('B', 'C')]:
    #     g.add_edge(u, v)
    # print(g)

    #
    # print("\nPDF - method remove_edge() / remove_vertex example 1")
    # print("----------------------------------------------------")
    # g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    # g.remove_vertex('DOES NOT EXIST')
    # g.remove_edge('A', 'B')
    # g.remove_edge('X', 'B')
    # print(g)
    # g.remove_vertex('D')
    # print(g)
    #
    #
    # print("\nPDF - method get_vertices() / get_edges() example 1")
    # print("---------------------------------------------------")
    # g = UndirectedGraph()
    # print(g.get_edges(), g.get_vertices(), sep='\n')
    # g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE'])
    # print(g.get_edges(), g.get_vertices(), sep='\n')

    #
    # print("\nPDF - method is_valid_path() example 1")
    # print("--------------------------------------")
    # g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    # test_cases = ['ABC', 'ADE', 'ECABDCBE', 'ACDECB', '', 'D', 'Z']
    # for path in test_cases:
    #     print(list(path), g.is_valid_path(list(path)))


    # print("\nPDF - method dfs() and bfs() example 1")
    # print("--------------------------------------")
    # edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    # g = UndirectedGraph(edges)
    # test_cases = 'ABCDEGH'
    # for case in test_cases:
    #     print(f'{case} DFS:{g.dfs(case)} BFS:{g.bfs(case)}')
    # print('-----')
    # for i in range(1, len(test_cases)):
    #     v1, v2 = test_cases[i], test_cases[-1 - i]
    #     print(f'{v1}-{v2} DFS:{g.dfs(v1, v2)} BFS:{g.bfs(v1, v2)}')

    #
    # print("\nPDF - method count_connected_components() example 1")
    # print("---------------------------------------------------")
    # edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    # g = UndirectedGraph(edges)
    # test_cases = (
    #     'add QH', 'remove FG', 'remove GQ', 'remove HQ',
    #     'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
    #     'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
    #     'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG')
    # for case in test_cases:
    #     command, edge = case.split()
    #     u, v = edge
    #     g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
    #     print(g.count_connected_components(), end=' ')
    # print()
    #
    #
    # print("\nPDF - method has_cycle() example 1")
    # print("----------------------------------")
    # edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    # g = UndirectedGraph(edges)
    # test_cases = (
    #     'add QH', 'remove FG', 'remove GQ', 'remove HQ',
    #     'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
    #     'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
    #     'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG',
    #     'add FG', 'remove GE')
    # for case in test_cases:
    #     command, edge = case.split()
    #     u, v = edge
    #     g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
    #     print('{:<10}'.format(case), g.has_cycle())
