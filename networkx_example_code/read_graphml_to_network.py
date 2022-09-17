
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# 参考：https://www.jb51.net/article/171825.htm
def color(value):
    digit = list(map(str, range(10))) + list("ABCDEF")
    if isinstance(value, tuple):
        string = '#'
        for i in value:
          a1 = i // 16
          a2 = i % 16
          string += digit[a1] + digit[a2]
        return string
    elif isinstance(value, str):
        a1 = digit.index(value[1]) * 16 + digit.index(value[2])
        a2 = digit.index(value[3]) * 16 + digit.index(value[4])
        a3 = digit.index(value[5]) * 16 + digit.index(value[6])
        return (a1, a2, a3)


# 定义获取节点坐标的函数
def get_node_coordinates(G):
    pos = {}
    x = nx.get_node_attributes(G, 'x')
    y = nx.get_node_attributes(G, 'y')
    for i in G.nodes():
        ix = x[i]
        iy = y[i]
        pos[i] = (ix, iy)  # 节点i的坐标

    return pos

def get_node_color(G):
    nodes_color = {}
    r = nx.get_node_attributes(G, 'r')
    g = nx.get_node_attributes(G, 'g')
    b = nx.get_node_attributes(G, 'b')
    for i in G.nodes():
        rgb_value = (r[i], g[i], b[i])
        nodes_color[i] = color(rgb_value)  # 节点i的颜色
    return nodes_color


G = nx.read_graphml("example.graphml")
print(G.edges())
# for e in G.edges():
edge_weight = nx.get_edge_attributes(G, 'weight')
nom_edge_weight = np.array(list(edge_weight.values()))/5

pos_nodes = get_node_coordinates(G)
nodes_color = get_node_color(G)

node_degree = dict(G.degree())
nodesize = np.array(list(node_degree.values()))*10
# print(nodesize)
# print(pos)
# print(nodes_color)

options = {
    'pos': pos_nodes,
    'node_size': nodesize,
    'node_color': nodes_color.values(),
    'edge_color': "gray",
    'with_labels': False,
    'node_shape': "s",
    'alpha': 0.8,
    'width': nom_edge_weight,
}


nx.draw(G, **options)
plt.show()