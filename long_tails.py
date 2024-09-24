import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import powerlaw


# Функция для построения случайной сети (замените на ваши данные)
def generate_random_graph(num_nodes=1000, prob=0.01):
    return nx.erdos_renyi_graph(num_nodes, prob)


# Построение сети
G = generate_random_graph()

# 1. Построение распределения степеней узлов
degrees = [G.degree(n) for n in G.nodes()]
plt.hist(degrees, bins=50, color='b', alpha=0.7)
plt.title("Распределение степеней узлов")
plt.xlabel("Степень узла")
plt.ylabel("Частота")
plt.show()

# 2. Построение кумулятивной функции распределения
degree_values = sorted(set(degrees))
hist = [degrees.count(x) for x in degree_values]
cdf = np.cumsum(hist) / sum(hist)
plt.plot(degree_values, cdf, marker='o', linestyle='none')
plt.title("Кумулятивная функция распределения степеней")
plt.xlabel("Степень узла")
plt.ylabel("CDF")
plt.show()

# 3. Оценка распределения с помощью степенной функции
fit = powerlaw.Fit(degrees, discrete=True)
alpha = fit.alpha
xmin = fit.xmin

print(f"Оценка параметров степенного распределения:")
print(f"Alpha: {alpha}")
print(f"x_min: {xmin}")

# Построение графика для степенного распределения
fig = fit.plot_ccdf(linewidth=3, color='b', label='Данные')
fit.power_law.plot_ccdf(ax=fig, color='r', linestyle='--', label='Степенной закон')
plt.legend()
plt.title("Оценка степенного распределения")
plt.show()

# 4. Вычисление центральностей узлов
degree_centrality = nx.degree_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)

# Вывод основных метрик узлов
print("Degree Centrality:", sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:5])
print("Closeness Centrality:", sorted(closeness_centrality.items(), key=lambda x: x[1], reverse=True)[:5])
print("Betweenness Centrality:", sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)[:5])

# Визуализация графа с окрашенными по степени узлами
plt.figure(figsize=(10, 10))
node_color = [degree_centrality[n] for n in G.nodes()]
nx.draw(G, node_color=node_color, cmap=plt.cm.Blues, node_size=50, with_labels=False)
plt.title("Визуализация графа с окраской по Degree Centrality")
plt.show()
