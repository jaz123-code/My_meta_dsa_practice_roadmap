def bfsG(graph,src,q,dst, visited):
    q.append(src)
    visited.add(src)

    while q:
        node=q.pop(0)
        if node==dst:
            return True
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.ppend(nei)
    return False

from collections import deque

def hasPathBFS(graph, src, dst):
    queue = deque([src])
    visited = set([src])

    while queue:
        node = queue.popleft()

        if node == dst:
            return True

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return False
