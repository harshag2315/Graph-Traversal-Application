import igraph as ig
import matplotlib.pyplot as plt
from algo import dijkstra, astar
def visualize_graph(g):
layout = g.layout("kk")
fig, ax = plt.subplots()
for edge, weight in zip(g.get_edgelist(), g.es["weight"]):
start = layout[edge[0]]
end = layout[edge[1]]
ax.plot([start[0], end[0]], [start[1], end[1]], color='gray', linestyle='-', linewidth=1)
ax.text((start[0] + end[0]) / 2, (start[1] + end[1]) / 2, str(weight), ha="center", va="center", fontsize=8, color="green")
for v in g.vs():
x, y = layout[v.index]
ax.text(x, y, f"{v['name']} ({v.index})", ha="center", va="center", fontsize=8, color="blue")
ax.add_artist(plt.Circle((x, y), 0.03, color='red', fill=False))
ax.text(x, y, str(v.index), ha="center", va="center", fontsize=8, color="red")
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
plt.axis('off')
return fig, ax
def main():
# Define the edges and their weights
edges = [(0,1), (0,2), (2,3), (3,4), (4,2), (2,5), (5,0), (6,3), (5,6)]
weights = [1, 4, 9, 5, 7, 8, 6, 2, 3]
# Create the graph
g = ig.Graph(edges)
g.vs["name"] = ["Paris", "New-York", "Denmark", "California", "Los Angeles", "London", "Maldives"]
g.es["weight"] = weights
print("\t\t\t***WELCOME TO THE COMMAND-LINE INTERFACE OF THE GRAPH TRAVERSAL*** ")
print("1. To start the application\n")
print("2. Display the graph for validation\n")
print("3. Exit\n")
choice = input("Enter your choice: ")
if choice == "1":
print("Enter the starting and ending node names:")
start_vertex_name = input("Start node: ")
end_vertex_name = input("End node: ")
start_vertex_index = g.vs.find(name=start_vertex_name).index
end_vertex_index = g.vs.find(name=end_vertex_name).index
try:
shortest_distance_dijkstra, shortest_path_dijkstra = dijkstra(g, start_vertex_index, end_vertex_index)
shortest_distance_astar, shortest_path_astar = astar(g, start_vertex_index, end_vertex_index)
if shortest_distance_dijkstra == shortest_distance_astar and shortest_path_dijkstra == shortest_path_astar:
print("Shortest path and cost found using both Dijkstra's and A* algorithms:\n")
print(f"Shortest distance: {shortest_distance_dijkstra}")
print("\nShortest path:", end=" ")
print(" -> ".join([g.vs[vertex_index]["name"] for vertex_index in shortest_path_dijkstra]))
else:
print("Shortest path and cost not found using both algorithms.")
except (ValueError, IndexError) as e:
print(e)
elif choice == "2":
fig, ax = visualize_graph(g)
plt.show()
elif choice == "3":
print("Exiting the program...")
return
else:
print("Invalid choice. Please try again.")
main()
if __name__ == "__main__":
main()