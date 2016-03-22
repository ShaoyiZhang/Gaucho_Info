import graphviz as gv
import functools
###
#g2 = gv.Digraph(format = 'svg')
#g2.node('CS')
#g2.node('B')
#g2.edge('A','B')
#g2.render('img/g2')
###

def add_nodes(graph, nodes):
	for n in nodes:
		if isinstance(n,tuple):
			graph.node(n[0], **n[1])
		else:
			graph.node(n)
	return graph

def add_edges(graph, edges):
	for e in edges:
		if isinstance(e[0],tuple):
			grpah.edge(*e[0], **e[1])
		else:
			graph.edge(*e)
		return graph

graph = functools.partial(gv.Graph, format = 'svg')
digraph = functools.partial(gv.Digraph, format = 'svg')

add_edges(
	add_nodes(digraph(),['CS8','CS16','CS24','CS32','CS40']),
			  [('CS16','CS24'), ('CS24','CS32'),('CS24','CS40')]
).render('img/g4')


#filename = g2.render(filename='img/g2')
#print filename