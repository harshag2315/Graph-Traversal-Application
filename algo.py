import heapq
def dijkstra(graph, start_vertex_index, end_vertex_index):
if start_vertex_index < 0 or start_vertex_index >= len(graph.vs):
raise ValueError("Invalid start vertex index.")
if end_vertex_index < 0 or end_vertex_index >= len(graph.vs):
raise ValueError("Invalid end vertex index.")
distances = {vertex.index: float('inf') for vertex in graph.vs}
distances[start_vertex_index] = 0
priority_queue = [(0, start_vertex_index)]
previous_vertices = {}
while priority_queue:
current_distance, current_vertex_index = heapq.heappop(priority_queue)
if current_distance > distances[current_vertex_index]:
continue
if current_vertex_index == end_vertex_index:
break
for neighbor, edge in zip(graph.neighbors(current_vertex_index), graph.es.select(_source=current_vertex_index)):
neighbor_vertex_index = neighbor
distance = current_distance + edge["weight"]
if distance < distances[neighbor_vertex_index]:
distances[neighbor_vertex_index] = distance
previous_vertices[neighbor_vertex_index] = current_vertex_index
heapq.heappush(priority_queue, (distance, neighbor_vertex_index))
path = []
current_vertex_index = end_vertex_index
while current_vertex_index in previous_vertices:
path.insert(0, current_vertex_index)
current_vertex_index = previous_vertices[current_vertex_index]
path.insert(0, start_vertex_index)
shortest_distance = distances[end_vertex_index]
return shortest_distance, path
def heuristic(graph, current_vertex_index, end_vertex_index):
# Simple heuristic that returns zero
return 0
def astar(graph, start_vertex_index, end_vertex_index):
if start_vertex_index < 0 or start_vertex_index >= len(graph.vs):
raise ValueError("Invalid start vertex index.")
if end_vertex_index < 0 or end_vertex_index >= len(graph.vs):
raise ValueError("Invalid end vertex index.")
distances = {vertex.index: float('inf') for vertex in graph.vs}
distances[start_vertex_index] = 0
priority_queue = [(0 + heuristic(graph, start_vertex_index, end_vertex_index), 0, start_vertex_index)]
previous_vertices = {}
while priority_queue:
_, current_distance, current_vertex_index = heapq.heappop(priority_queue)
if current_distance > distances[current_vertex_index]:
continue
if current_vertex_index == end_vertex_index:
break
for neighbor, edge in zip(graph.neighbors(current_vertex_index), graph.es.select(_source=current_vertex_index)):
neighbor_vertex_index = neighbor
distance = current_distance + edge["weight"]
if distance < distances[neighbor_vertex_index]:
distances[neighbor_vertex_index] = distance
previous_vertices[neighbor_vertex_index] = current_vertex_index
heapq.heappush(priority_queue, (distance + heuristic(graph, neighbor_vertex_index, end_vertex_index), distance, neighbor_vertex_index))
path = []
current_vertex_index = end_vertex_index
while current_vertex_index in previous_vertices:
path.insert(0, current_vertex_index)
current_vertex_index = previous_vertices[current_vertex_index]
path.insert(0, start_vertex_index)
shortest_distance = distances[end_vertex_index]
return shortest_distance, path