from collections import defaultdict, deque, Counter
from functools import cache
import heapq
import math
import sys
import re
import networkx as nx

dirs = [(-1,0),(0,1),(1,0),(0,-1)] # up right down left

# cp template.py day_no.py
# https://topaz.github.io/paste/
# time <python_file.py>
# python3 -m <python_file>
# python3 -m <python_file> <inp.txt>

def pr(data):
	print("data ", data)

def print_grid(grid):
	# [print(row) for row in grid]
	[print("".join(row)) for row in grid]

def part1(graph):
	# dfs and find cyclic graphs with size 3
	candidates = []
	def dfs(node, path, start):
		# print('called dfs ', node, path, start)
		
		if len(path) == 3:
			# print("got 3 items ", path)
			for neighbour in graph[node]:
				if neighbour == start:
					# candidates.append(set(path)
					# print("path ", sorted(path))
					sp = sorted(path)
					if sp not in candidates:
						candidates.append(sp)
			return

		for neighbour in graph[node]:
			if neighbour not in path:
				path.append(neighbour)
				dfs(neighbour, path, start)
				path.pop()
		return

	for key, val in graph.items():
		dfs(key, [key], key)

	[print(candidate) for candidate in candidates]
	print(len(candidates))
	ans = 0
	for a, b, c in candidates:
		if a[0] == "t" or b[0] == "t" or c[0] == "t":
			ans += 1
	print(ans)



class DisjointSet:
    def __init__(self, items):
        """
        Initialize the disjoint set with a list of items.
        Each item starts as its own parent, with rank 0 and size 1.
        """
        self.item_to_index = {item: i for i, item in enumerate(items)}  # Map items to indices
        self.index_to_item = {i: item for i, item in enumerate(items)}  # Map indices back to items
        self.parent = [i for i in range(len(items))]  # Each element is its own parent initially
        self.rank = [0] * len(items)  # Rank for union by rank optimization
        self.size = [1] * len(items)  # Size of each set, initially 1

    def find(self, item):
        """
        Find the representative (root) of the set containing the item with path compression.
        """
        index = self.item_to_index[item]
        if self.parent[index] != index:
            self.parent[index] = self.find(self.index_to_item[self.parent[index]])  # Path compression
        return self.parent[index]

    def union(self, item1, item2):
        """
        Union the sets containing item1 and item2.
        Uses union by rank to keep the tree shallow and updates the size of the root.
        """
        root1 = self.find(item1)
        root2 = self.find(item2)

        if root1 != root2:
            # Union by rank
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
                self.size[root1] += self.size[root2]  # Update size
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
                self.size[root2] += self.size[root1]  # Update size
            else:
                self.parent[root2] = root1
                self.size[root1] += self.size[root2]  # Update size
                self.rank[root1] += 1

    def connected(self, item1, item2):
        """
        Check if item1 and item2 are in the same set.
        """
        return self.find(item1) == self.find(item2)

    def component_size(self, item):
        """
        Get the size of the entire connected component containing the item.
        """
        root_index = self.find(item)
        return self.size[root_index]

    def get_connected_nodes(self, item):
        """
        Get all nodes in the same connected component as the given item.
        """
        root = self.find(item)
        return [node for node in self.item_to_index if self.find(node) == root]




def part2(graph, data):
	candidates = []
	with_t = set()
	def dfs(node, path, start):
		if len(path) == 3:
			for neighbour in graph[node]:
				if neighbour == start:
					for key in path:
						if key[0] == "t":
							for key in path:
								with_t.add(key)							
							sp = sorted(path)
							if sp not in candidates:
								candidates.append(sp)
							break

			return

		for neighbour in graph[node]:
			if neighbour not in path:
				path.append(neighbour)
				dfs(neighbour, path, start)
				path.pop()
		return

	for key, val in graph.items():
		dfs(key, [key], key)

	print("candidates ", candidates)
	print("with_t ", with_t)
	dsu = DisjointSet(list(with_t))

	max_item = None
	max_size = -1
	for a, b, c in candidates:
		dsu.union(a,b)
		dsu.union(b,c)
		
		size = dsu.component_size(a)
		print('connecting  ', a, b, c)
		print("lets examine connections ", dsu.get_connected_nodes(a))
		if size > max_size:
			max_size = size
			max_item = a
	
	print(max_item)
	print(max_size)

	conn = dsu.get_connected_nodes(max_item)
	print(conn)
	# print(leaders)
	# print(list(keys))
	# print(ans)



def part2(data):
	# max clique problem
	graph = nx.Graph()
	for line in data:
		u, v = line.split("-")
		graph.add_edge(u,v)
		graph.add_edge(v,u)

	max_clique = ()
	for clique in nx.find_cliques(graph):
		if len(clique) > len(max_clique):
			max_clique = clique
	ans = ",".join(sorted(max_clique))
	print("ans is ", ans)




if __name__ == "__main__":	
	file = "eg.txt"
	file = "in.txt"
	file = sys.argv[1] if len(sys.argv)>=2 else file
	data = open(file, "r").read().split("\n")
	graph = defaultdict(list)
	for line in data:
		u, v = line.split("-")
		graph[u].append(v)
		graph[v].append(u)
	# print(graph)
	# part1(graph)

	# part2(graph, data)
	part2(data)




# # Example Usage
# if __name__ == "__main__":
#     # Create a disjoint set with a list of items
#     items = ["ab", "gf", "ea"]
#     ds = DisjointSet(items)

#     # Perform unions
#     ds.union("ab", "gf")  # Merge {"ab"} and {"gf"}
#     ds.union("gf", "ea")  # Merge {"ab", "gf"} and {"ea"}

#     # Find the size of the connected components
#     print(ds.component_size("ab"))  # Output: 3 (connected component: {"ab", "gf", "ea"})
#     print(ds.component_size("ea"))  # Output: 3 (connected component: {"ab", "gf", "ea"})

#     # Check if items are connected
#     print(ds.connected("ab", "ea"))  # Output: True
#     print(ds.connected("ab", "zz"))  # Output: False (KeyError if "zz" not in items)


# # Example Usage
# if __name__ == "__main__":
#     # Create a disjoint set with a list of items
#     items = ["ab", "gf", "ea", "xy", "mn"]
#     ds = DisjointSet(items)

#     # Perform unions
#     ds.union("ab", "gf")  # Merge {"ab"} and {"gf"}
#     ds.union("gf", "ea")  # Merge {"ab", "gf"} and {"ea"}
#     ds.union("xy", "mn")  # Merge {"xy"} and {"mn"}

#     # Get all connected nodes
#     print(ds.get_connected_nodes("ab"))  # Output: ['ab', 'gf', 'ea']
#     print(ds.get_connected_nodes("xy"))  # Output: ['xy', 'mn']
#     print(ds.get_connected_nodes("mn"))  # Output: ['xy', 'mn']
#     print(ds.get_connected_nodes("ea"))  # Output: ['ab', 'gf', 'ea']

