import networkx as nx
import matplotlib.pyplot as plt

# Параметры модели Эрдеша-Реньи
n = 100  # количество узлов
p = 0.05  # вероятность появления ребра

er_model = nx.erdos_renyi_graph(n, p)


def draw_graph(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='gray')
    plt.show()


draw_graph(er_model)

print(f"Средняя степень узлов: {sum(dict(er_model.degree()).values())/n}")
print(f"Средняя длина пути: {nx.average_shortest_path_length(er_model)}")
print(f"Коэффициент кластеризации: {nx.average_clustering(er_model)}")
