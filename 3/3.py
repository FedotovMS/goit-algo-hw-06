import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Створення графа метро Амстердама з вагами
G = nx.Graph()

# Станції метро Амстердама
stations = [
    "Centraal Station", "Rokin", "Spui", "Dam", "Nieuwmarkt", "Waterlooplein", "Muziektheater", 
    "Weesperplein", "Amstel", "Duivendrecht", "Zuid", "WTC", "Hendrik de Keijser", "Sloterdijk", 
    "Haarlemmermeerstation", "Jan van Galenstraat", "Lelylaan", "Bijlmer Arena", "Noord", "Hallepoort", 
    "Amstel", "Rai", "Vanderkerckhove", "Uithoorn", "Geuzenveld", "Pijp"
]

# Додавання станцій у граф
G.add_nodes_from(stations)

# Додавання з'єднань між станціями з вагами до ребер
edges_with_weights = [
    ("Centraal Station", "Rokin", 2), ("Rokin", "Spui", 1), ("Spui", "Dam", 1), ("Dam", "Nieuwmarkt", 1),
    ("Nieuwmarkt", "Waterlooplein", 1), ("Waterlooplein", "Muziektheater", 2), ("Muziektheater", "Weesperplein", 3),
    ("Weesperplein", "Amstel", 2), ("Amstel", "Duivendrecht", 1), ("Duivendrecht", "Zuid", 2),
    ("Zuid", "WTC", 2), ("WTC", "Hendrik de Keijser", 3), ("Hendrik de Keijser", "Sloterdijk", 4),
    ("Sloterdijk", "Haarlemmermeerstation", 2), ("Haarlemmermeerstation", "Jan van Galenstraat", 2),
    ("Jan van Galenstraat", "Lelylaan", 3), ("Lelylaan", "Bijlmer Arena", 4), ("Bijlmer Arena", "Noord", 3),
    ("Noord", "Hallepoort", 3), ("Hallepoort", "Amstel", 1), ("Amstel", "Rai", 2), ("Rai", "Vanderkerckhove", 5),
    ("Vanderkerckhove", "Uithoorn", 4), ("Uithoorn", "Geuzenveld", 3), ("Geuzenveld", "Pijp", 2)
]

# Додавання ребер з вагами до графа
G.add_weighted_edges_from(edges_with_weights)

# Алгоритм Дейкстри
def dijkstra(graph, start):
    # Створюємо словник для зберігання найкоротших відстаней від початкової вершини
    shortest_paths = {node: float('inf') for node in graph.nodes()}
    shortest_paths[start] = 0

    # Черга пріоритету для вибору вузла з найменшою відстанню
    priority_queue = [(0, start)]  # (distance, node)
    
    while priority_queue:
        # Вибираємо вузол з мінімальною відстанню
        current_distance, current_node = heapq.heappop(priority_queue)

        # Якщо поточна відстань більша за вже знайдену, пропускаємо вузол
        if current_distance > shortest_paths[current_node]:
            continue

        # Перевіряємо всі суміжні вершини
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight['weight']

            # Якщо знайшли коротший шлях до сусіда, оновлюємо відстань
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return shortest_paths

# Тестування алгоритму Дейкстри для різних станцій
start_station = "Centraal Station"
shortest_paths = dijkstra(G, start_station)

# Виведення найкоротших шляхів від "Centraal Station" до всіх інших станцій
print(f"Найкоротші шляхи від {start_station}:")
for station, distance in shortest_paths.items():
    print(f"{start_station} -> {station}: {distance}")

# Візуалізація графа з вагами
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G, seed=42)  # Позиціонування вузлів для кращого вигляду
nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue', alpha=0.7)
nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=10, font_family="Arial")

# Візуалізація ваг на ребрах
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Мережа метро Амстердама з вагами до ребер")
plt.axis('off')
plt.show()