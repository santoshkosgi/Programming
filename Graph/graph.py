"""
This script returns a graph data structure which can be used for implementing searching on top of it.
We can move in all the directions except for diagonals.
"""
import networkx as nx
from matplotlib import pyplot as plt


class Graph(object):
    def __init__(self, grid_size=10):
        self.grid_size = grid_size
        self.G = nx.grid_2d_graph(grid_size, grid_size)


    def draw_graph(self, list_of_obstacles, edge_list, node_lables, src_node, dest_node):
        """
        This function draws a graph given lables of the node, edges list and list of obstacles which are
        colored differently
        @param list_of_obstacles: list of nodes which cannot be passed through
        @param edge_list: list edges that needs to be drawn
        @param node_lables: Lables of the node
        @param src_node: start node for the search algorithm
        @param dest_node: Destination node for the search algorithm
        @return: Draws a graph using networkx
        """
        self.G = self.G.to_directed()
        plt.figure(figsize=(6, 6))
        pos = {(x, y): (x, y) for x, y in self.G.nodes()}
        nx.draw_networkx_nodes(self.G, pos=pos, node_color='lightgreen',
                               nodelist=self.G.nodes(), node_size=600)
        nx.draw_networkx_nodes(self.G, pos=pos, node_color='lightblue',
                               nodelist=list_of_obstacles, node_size=600)
        nx.draw_networkx_labels(self.G, pos, node_lables, font_size=6, font_color='r')

        nx.draw_networkx_edges(self.G, pos=pos, edgelist=edge_list)
        plt.show()

    def bfs(self, list_of_obstacles, src_node, dest_node, node_labels):
        """
        This function a BFS search from src_node to dest node.
        @param list_of_obstacles: List of nodes, which cant be passed.
        @param src_node: source node from where the search should start
        @param dest_node: destination node of the search.
        @return: calls draw graph function to plot the search path, nodes explored etc.
        """
        queue = []
        queue.append((src_node, None))
        nodes_seen = set()

        edge_list = []

        found_dest = False

        while len(queue) > 0 and found_dest is False:
            curr_node, parent = queue.pop(0)
            if curr_node in nodes_seen:
                continue
            if parent is not None:
                edge_list.append((parent, curr_node))
            nodes_seen.add(curr_node)
            neighbours = self.G.neighbors(curr_node)
            for neighbour in neighbours:
                if neighbour not in list_of_obstacles and neighbour not in nodes_seen:
                    queue.append((neighbour,curr_node))
                    if neighbour == dest_node:
                        edge_list.append((curr_node, neighbour))
                        found_dest = True
                        break
        self.draw_graph(list_of_obstacles, edge_list, node_labels, src_node, dest_node)


if __name__ == '__main__':
        graph = Graph(10)
        labels = {}
        for node in graph.G.nodes():
            labels[node] = node
        list_of_obs = [ (6,1), (6,2), (6,3), (6,4), (6,5), (6,6), (6,8)]
        edge_list  = [((2,3), (3,4))]
        graph.bfs(list_of_obstacles=list_of_obs, src_node=(0, 0), dest_node=(6,2), node_labels=labels)
        # graph.draw_graph(list_of_obstacles=list_of_obs, edge_list=edge_list, node_lables=labels, src_node=(0, 0),
        #              dest_node=(9, 4))






