import networkx as nx
import matplotlib.pyplot as plt

# Створення порожнього графа
G = nx.Graph()

# Додавання станцій метро Амстердама як вузлів
stations = [
    "Centraal Station", "Rokin", "Spui", "Dam", "Nieuwmarkt", "Waterlooplein", "Muziektheater", 
    "Weesperplein", "Amstel", "Duivendrecht", "Zuid", "WTC", "Hendrik de Keijser", "Sloterdijk", 
    "Haarlemmermeerstation", "Jan van Galenstraat", "Lelylaan", "Bijlmer Arena", "Noord", "Hallepoort", 
    "Amstel", "Rai", "Vanderkerckhove", "Uithoorn", "Geuzenveld", "Pijp"
]

# Додавання станцій у граф
G.add_nodes_from(stations)

# Додавання з'єднань між станціями як ребра
edges = [
    ("Centraal Station", "Rokin"), ("Rokin", "Spui"), ("Spui", "Dam"), ("Dam", "Nieuwmarkt"),
    ("Nieuwmarkt", "Waterlooplein"), ("Waterlooplein", "Muziektheater"), ("Muziektheater", "Weesperplein"),
    ("Weesperplein", "Amstel"), ("Amstel", "Duivendrecht"), ("Duivendrecht", "Zuid"),
    ("Zuid", "WTC"), ("WTC", "Hendrik de Keijser"), ("Hendrik de Keijser", "Sloterdijk"),
    ("Sloterdijk", "Haarlemmermeerstation"), ("Haarlemmermeerstation", "Jan van Galenstraat"),
    ("Jan van Galenstraat", "Lelylaan"), ("Lelylaan", "Bijlmer Arena"), ("Bijlmer Arena", "Noord"),
    ("Noord", "Hallepoort"), ("Hallepoort", "Amstel"), ("Amstel", "Rai"), ("Rai", "Vanderkerckhove"),
    ("Vanderkerckhove", "Uithoorn"), ("Uithoorn", "Geuzenveld"), ("Geuzenveld", "Pijp")
]

# Додавання ребер до графа
G.add_edges_from(edges)

# Візуалізація графу
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G, seed=42)  # Позиціонування вузлів для кращого вигляду
nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue', alpha=0.7)
nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=10, font_family="Arial")
plt.title("Мережа метро Амстердама")
plt.axis('off')
plt.show()

# Аналіз характеристик мережі
print(f"Кількість станцій (вершин): {G.number_of_nodes()}")
print(f"Кількість з'єднань (ребер): {G.number_of_edges()}")
degree = dict(G.degree())
print(f"Ступені вершин (кількість з'єднань кожної станції): {degree}")