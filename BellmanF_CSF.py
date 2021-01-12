# @Rexhino_Kovaci
# Implementing Bellman-Ford Algorithm on the Graph Class and Creating def functions
# to add Eddges and Calculate the vertixes and display the array created by the Vertex Distance
# Bellman - Ford Algorithm is a "Greedy Algorithm" that only chooses the least costs edge of the vertex


class GraphBellman:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []


        # this would construct our V - parameter with vertices and create the graph

        # function to add an edge to graph

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

        # a def function to add the edges with the parameters u, v and w

    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

            # a def function to print the Array and the vertex distance from the source

    # the vertices using Bellman Ford Algorithm detects the negative weight costs in the cycle

    def BellmanFord(self, src):

        # we initialize the source with a float pointing number
        dist = [float("Inf")] * self.V
        dist[src] = 0

        #  relax all edges |V| - 1 times. A simple shortest
        # path from src to any other vertex can have at-most v - 1
        for _ in range(self.V - 1):
            # update the values and the index
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        #    check for the negative values

        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return

        # print all distance  
        self.printArr(dist)


g = GraphBellman(4)
g.addEdge(1, 0, 1)
g.addEdge(0, 1, -1)
g.addEdge(1, 0, 1)
g.addEdge(0, 2, 1)
g.addEdge(3, 1, 2)
g.addEdge(2, 1, 4)
g.addEdge(0, 1, 3)
g.addEdge(1, 1, 2)

g.BellmanFord(3)
#  print the solution we got