from collections import deque
def cycle(graph):
    visited=set()
    for node in graph:
        if node in visited:
            continue
        n=deque([(node,-1)])
        visited.add(node)
        while n:
            curr, parent=n.popleft()
            for nei in graph[curr]:
                if nei==parent:
                    continue
                if nei in visited:
                    return True
                visited.add(nei)
                n.append((nei, curr))
    return False
                
