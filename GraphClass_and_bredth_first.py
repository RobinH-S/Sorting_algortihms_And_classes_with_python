
#Class Graph representing a graph object with nodes. And functions for getting neighour nodes and bredth_first search.
class Graph:
    graph = dict()
    def add_edge(self, node, neighbour):
        #Adding a a new node and connecting it to a neighbour
        if node not in self.graph:
            self.graph[node] = [neighbour]
        else:
            self.graph[node].append(neighbour)

    def print_graph(self):
        print(self.graph)


    #method to run Breadth First Search (BFS) starting from node 1 and printing out all the nodes.
    def bredth_first_search(self, node):
        searched = []
        search_queue = [node]

        while search_queue:
            searched.append(node)
            node = search_queue.pop(0)

            print("[", node, end="] , ")

            for neighbour in self.graph[node]:
                if neighbour not in searched:
                    searched.append(neighbour)
                    search_queue.append(neighbour)


#creating a graph and adding edges
my_graph = Graph()
my_graph.add_edge('1', '2')
my_graph.add_edge('1', '3')
my_graph.add_edge('2', '3')
my_graph.add_edge('2', '4')
my_graph.add_edge('3', '5')
my_graph.add_edge('4', '5')
my_graph.add_edge('5', '6')
my_graph.add_edge('6', '3')

i=1

while i < len(my_graph.graph):
    i = str(i)
    my_graph.bredth_first_search(i)
    print('')
    i= int(i)
    i = i +1

#function to build a graph with nodes and edges
def build_my_graph2():
    my_graph = Graph()
    my_graph.add_edge('1', '2')
    my_graph.add_edge('1', '3')
    my_graph.add_edge('2', '3')
    my_graph.add_edge('2', '4')
    my_graph.add_edge('3', '5')
    my_graph.add_edge('4', '5')
    my_graph.add_edge('5', '6')
    my_graph.add_edge('6', '3')




#Using the build_my_graph2 function to build a graph
build_my_graph2()