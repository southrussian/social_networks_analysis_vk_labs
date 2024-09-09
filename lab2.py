import networkx as nx
import matplotlib.pyplot as plt

# Параметры модели Барабаши-Альберта
n = 100  # количество узлов
m = 3    # количество ребер, добавляемых к новому узлу

ba_model = nx.barabasi_albert_graph(n, m)


def draw_graph(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='gray')
    plt.show()


draw_graph(ba_model)

print(f"Средняя степень узлов: {sum(dict(ba_model.degree()).values())/n}")
print(f"Средняя длина пути: {nx.average_shortest_path_length(ba_model)}")
print(f"Коэффициент кластеризации: {nx.average_clustering(ba_model)}")
