import heapq
def dijkstra(graph, start):
    shortest_paths = {vertex: float('inf') for vertex in graph}
    shortest_paths[start] = 0
    pq = [(0, start)]
    while pq:
        (cost, vertex) = heapq.heappop(pq)
        for neighbor, weight in graph[vertex].items():
            new_cost = cost + weight
            if new_cost < shortest_paths[neighbor]:
                shortest_paths[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))
    return shortest_paths
traffic_graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'C': 3, 'D': 2},
    'C': {'D': 1},
    'D': {'E': 4},
    'E': {}
}
start_point = 'A'
optimal_routes = dijkstra(traffic_graph, start_point)
print(f"Optimal travel times from {start_point}:")
for dest, time in optimal_routes.items():
    print(f"To {dest}: {time} minutes")
