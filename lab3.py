import networkx as nx
import matplotlib.pyplot as plt

# Параметры модели Уоттса-Строгатца
n = 100  # количество узлов
k = 6    # средняя степень узла
p = 0.1  # вероятность перемешивания связей


ws_model = nx.watts_strogatz_graph(n, k, p)


def draw_graph(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='gray')
    plt.show()


draw_graph(ws_model)

print(f"Средняя степень узлов: {sum(dict(ws_model.degree()).values())/n}")
print(f"Средняя длина пути: {nx.average_shortest_path_length(ws_model)}")
print(f"Коэффициент кластеризации: {nx.average_clustering(ws_model)}")
