from collections import deque

def shortp(graph, src, dst):
    # Queue stores tuples of (current_node, current_distance)
    q = deque([(src, 0)])
    visited = set([src])

    while q:
        node, dis = q.popleft()

        if node == dst:
            return dis

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                # FIX: Use 'dis + 1' directly in the append call.
                # Do not modify 'dis' itself.
                q.append((nei, dis + 1))
    
    return -1  # Return -1 if destination is unreachable
