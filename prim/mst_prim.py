import numpy as np

class Graph():
    def __init__(self, nodes_num):
        self.nodes_num = nodes_num
        self.graph = [[0]*self.nodes_num]*self.nodes_num

    def primMST(self):
        #the list of vectors already added to the tree
        mstSET = []
        mstEDGES = []
        #we initialize the values at node 0
        mstSET.append(0)
        #the loop stops when mstSET contains all the nodes
        current_node = 0
        while len(mstSET) != len(self.graph):
            adjacent_nodes = [x if (x != 0 and i not in mstSET) else 99 for i, x in enumerate(self.graph[current_node]) ]
            min_distance_node = np.argmin(adjacent_nodes)
            edge = (current_node, min_distance_node)
            mstEDGES.append(edge)
            mstSET.append(min_distance_node)
            current_node = min_distance_node
        return mstEDGES

if __name__ == '__main__':
    g = Graph(4)
    g.graph = [
            [0, 0.4, 0, 0.4],
            [0.4, 0, 0.3, 0.1],
            [0, 0.3, 0, 0.5],
            [0.4, 0.1, 0.5, 0]
            ]
    print(g.primMST())
