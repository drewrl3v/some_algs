# Graphs (DFS)


## Perform a DFS traversal of a given graph (Recursive)

You are given a `graph` as an adjacency list and a vertex `s` in the graph.
Traverse its nodes via DFS.

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

def dfs(s, graph):
    seen = set()
    def traverse(s):
        if s not in seen:
            print(s)
            seen.add(s)
            for node in graph[s]:
                traverse(node)
    traverse(s)


</code></pre>
</details>


## Perform a DFS traversal of a given graph (Iterative)

Implement an iterative DFS traversal of `graph` startin at vertex `s`.


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

def dfs(s, graph):
    seen = set()
    stack = [s]
    while stack:
        node = stack.pop()
        if node not in seen:
            print(node)
            seen.add(node)
            # can call reversed to here to match previous solution
            for neighbor in graph[node]: 
                if neighbor not in seen:
                    stack.append(neighbor)

</code></pre>
</details>

