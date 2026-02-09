# Graphs (BFS)


## Perform a BFS traversal of a given graph

You are given a `graph` as an adjacency list and a vertex `s` in the graph.
Traverse its nodes via a BFS. Note: this problem doesn't care about the order 
in which you traverse a layer during the BFS, so it's not necessary to use a queue.


<details>
<summary>Solution</summary>

<pre><code class="language-python">
graph = {
    1: [2,3],
    2: [1,3,4,5],
    3: [1,2,5,7,8],
    4: [2,5],
    5: [2,3,4,6],
    6: [5],
    7: [3,8],
    8: [3,7],
}

def bfs_no_queue(s, graph):
    discovered = set()
    discovered.add(s)
    current_layer = [s]

    while current_layer:
        print(current_layer)
        next_layer = []
        for node in current_layer:
            for next_node in graph[node]:
                if next_node not in discovered:
                    discovered.add(next_node)
                    next_layer.append(next_node)
        current_layer = next_layer

bfs_no_queue(1, graph)
</code></pre>
</details>

