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

# Алгоритм DFS (глибина)
def dfs(graph, start, end, path=[]):
    """
    Алгоритм пошуку в глибину (DFS).
    Повертає шлях від вузла start до вузла end в графі.
    Якщо шлях знайдений, повертає список вузлів шляху.
    Якщо шлях неможливий, повертає None.
    """
    path = path + [start]  # Додаємо поточний вузол в шлях
    if start == end:  # Якщо досягли кінцевої станції, повертаємо шлях
        return path
    if start not in graph:  # Якщо вузол не в графі, повертаємо None
        return None
    for node in graph[start]:  # Перевіряємо кожного сусіда поточного вузла
        if node not in path:  # Якщо сусід не відвіданий, рекурсивно шукаємо шлях
            new_path = dfs(graph, node, end, path)
            if new_path:  # Якщо шлях знайдений, повертаємо його
                return new_path
    return None  # Якщо шлях не знайдений, повертаємо None

# Алгоритм BFS (ширина)
def bfs(graph, start, end):
    """
    Алгоритм пошуку в ширину (BFS).
    Повертає найкоротший шлях від вузла start до вузла end в графі.
    Якщо шлях знайдений, повертає список вузлів шляху.
    Якщо шлях неможливий, повертає None.
    """
    visited = []  # Список для збереження відвіданих вузлів
    queue = [[start]]  # Черга для пошуку шляхів, спочатку містить тільки стартовий вузол
    
    if start == end:  # Якщо стартова станція є кінцевою, повертаємо список з одним елементом
        return [start]
    
    while queue:  # Поки є шляхи в черзі
        path = queue.pop(0)  # Вибираємо перший шлях з черги
        node = path[-1]  # Останній вузол в поточному шляху
        
        if node not in visited:  # Якщо вузол ще не відвіданий
            neighbors = graph[node]  # Отримуємо всіх сусідів поточного вузла
            for neighbor in neighbors:
                new_path = list(path)  # Копіюємо поточний шлях
                new_path.append(neighbor)  # Додаємо сусіда до шляху
                queue.append(new_path)  # Додаємо новий шлях в чергу
                
                if neighbor == end:  # Якщо досягли кінцевої станції, повертаємо шлях
                    return new_path
            visited.append(node)  # Додаємо поточний вузол до відвіданих
    return None  # Якщо шлях не знайдений, повертаємо None

# Вибір стартових та кінцевих станцій для пошуку
start_station = "Centraal Station"
end_station = "Lelylaan"

# Виконання DFS та BFS
dfs_path = dfs(G, start_station, end_station)
bfs_path = bfs(G, start_station, end_station)

# Виведення результатів
print(f"Шлях від {start_station} до {end_station} за допомогою DFS: {dfs_path}")
print(f"Шлях від {start_station} до {end_station} за допомогою BFS: {bfs_path}")

# Пояснення результатів
print("\nПояснення:")
print("-" * 50)
print("1. Алгоритм DFS (Пошук в глибину):")
print("   - Алгоритм DFS намагається пройти глибше, досліджуючи один шлях повністю до кінця.")
print("   - Якщо зустрічається кілька варіантів шляхів, DFS обирає перший, який може привести до кінцевої станції.")
print("   - Тому шлях за DFS не завжди є найкоротшим.")
print("   - У нашому випадку DFS може пройти через кілька зайвих станцій, перш ніж знайде правильний шлях.")
print("\n2. Алгоритм BFS (Пошук в ширину):")
print("   - Алгоритм BFS обходить всі можливі шляхи рівнями, гарантує, що перший знайдений шлях буде найкоротшим.")
print("   - BFS досліджує граф по рівнях, покриваючи більш близькі вузли до кінцевої станції.")
print("   - Таким чином, BFS дає оптимальний результат для найкоротшого шляху між двома станціями.")
print("-" * 50)

# Візуалізація графа з виділеними шляхами
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G, seed=42)  # Позиціонування вузлів для кращого вигляду
nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue', alpha=0.7)
nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color='gray')

# Виділяємо шляхи DFS та BFS на графі
dfs_edges = list(zip(dfs_path, dfs_path[1:])) if dfs_path else []
bfs_edges = list(zip(bfs_path, bfs_path[1:])) if bfs_path else []

# Червоним кольором позначаємо шляхи DFS
nx.draw_networkx_edges(G, pos, edgelist=dfs_edges, edge_color='red', width=2)
# Зеленим кольором позначаємо шляхи BFS
nx.draw_networkx_edges(G, pos, edgelist=bfs_edges, edge_color='green', width=2)

# Позначення станцій на графі
nx.draw_networkx_labels(G, pos, font_size=10, font_family="Arial")
plt.title("Мережа метро Амстердама з шляхами DFS (червоний) та BFS (зелений)")
plt.axis('off')
plt.show()