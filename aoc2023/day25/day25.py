data = open('input.txt', 'r').read().split('\n')
import networkx as nx

def part1(data):
	# print(data)
	adj = {}
	for line in data:
		line = line.replace(':', '')
		line = line.split(' ')
		# print(line)
		for item in line[1:]:
			if line[0] not in adj: adj[line[0]] = []
			if item not in adj: adj[item] = []

			adj[line[0]].append(item)
			adj[item].append(line[0])
	
	# print('adj list is')
	# [print(k,v) for k,v in adj.items()]
	
	G = nx.DiGraph()
	for k, value in adj.items():
		for v in value:
			G.add_edge(k, v, capacity=1.0) 
			G.add_edge(v, k, capacity=1.0)
	# print(list(adj.keys())) 

	# go to all the keys of the adj; try splitting it 3 ways
	
	keys = list(adj.keys())
	k1 = keys[0]
	for k2 in keys[1:]:
		cut_value, (L, R) = nx.minimum_cut(G, k1, k2)
		if cut_value == 3:
			print(len(L)*len(R))
			break



part1(data)