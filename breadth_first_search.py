from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E', 'F'],
    'C': ['G'],
    'D': [],
    'E': [],
    'F': ['H'],
    'G': ['I'],
    'H': [],
    'I': []
}


def breadth_first_search(graph, node):
    visited = set()
    queue = deque()

    # append starting node
    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.popleft()
        print(s, end=" ")

        for n in graph[s]:
            if n not in visited:
                visited.add(n)
                queue.append(n)


breadth_first_search(graph, "A")
