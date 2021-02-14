// Guide: https://www.techiedelight.com/graph-implementation-using-stl/
#include <iostream>
#include <vector>

using namespace std;

// data structure to store graph edges
struct Edge {
    int src, dest, weight;
};

typedef pair<int, int> Pair;

// class to represent a graph object
class Graph {
    public:
        // construct a vector of vectors to represent a adjacency list
        vector<vector<Pair> > adjList;

        // graph constructor
        Graph(vector<Edge> &edges, int N) {
            // resize the vector no N elements of type vector<int>
            adjList.resize(N);

            // add edges to the directed graph
            for (auto &edge: edges) {
                int src = edge.src;
                int dest = edge.dest;
                int weight = edge.weight;

                // insert at the end
                adjList[src].push_back(make_pair(dest, weight));
            }
        }
};

//print adjacency list representation of a graph
void print_graph(Graph const& graph, int N) {
    for (int i = 0; i != N; ++i) {
        // print current vertex number
        cout << i << " --> ";

        // print all neighboring vertices of vertex i
        for(Pair v : graph.adjList[i])
            cout << "(" << i << ", " << v.first << ", " << v.second << ") ";
        cout << endl;
    }
}

// Demo time
int main()
{
    vector<Edge> e = {
        {0,1,6}, {1,2,7}, {2,0,5}, {2,1,4}, {3,2,10}, {4,5,1}, {5,4,3}
    };

    int N = 6; // number of nodes in the graph

    // construct graph
    Graph g(e, N);

    print_graph(g, N);
    return 0;
}

