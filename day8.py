from collections import deque
def countComponent(graph):
    visited=set()
    count=0

    for node in graph:
        if node not in visited:
            queue=deque([node])
            visited.add(node)
            while queue:
                curr=queue.popleft()
                for nei in graph[curr]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
            components+=1
    return components