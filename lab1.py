import vk_api
import networkx as nx
import matplotlib.pyplot as plt

# vk1.a.HsuFagpssoZNlGtHR3lHV9ZKZ8z0M1qefv6SZ1fhBe3XJS83x6B8XpIxG7q-CwVcgu8iV0e2YlQpz3TVQfyolSiCrAaywcjRTtZKJ7Roqc6D5ZRouPPPILmvuFtdkAu0jOS81iM1ygB5VvubeyA1s8t3jJ0-wBGj0GlkiIvwSUvg2jTGx5NfbgRddv5lOir6Nrsmm-8ukqHZFK5Q1R7-AA
ACCESS_TOKEN = 'твой_access_token'

vk_session = vk_api.VkApi(token=ACCESS_TOKEN)
vk = vk_session.get_api()

# 221066680
user_id = 'ID пользователя'


def get_friends(user_id):
    try:
        friends = vk.friends.get(user_id=user_id, fields="domain")['items']
        return friends
    except vk_api.exceptions.ApiError as e:
        print(f"Ошибка: {e}")
        return []


def build_graph(user_id):
    friends = get_friends(user_id)
    G = nx.Graph()
    G.add_node(user_id)

    for friend in friends:
        friend_id = friend['id']
        G.add_node(friend_id)
        G.add_edge(user_id, friend_id)

    return G


def draw_graph(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='gray')
    plt.show()


graph = build_graph(user_id)
draw_graph(graph)