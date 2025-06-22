import networkx as nx
import matplotlib.pyplot as plt
import random

# Створюємо граф
G = nx.Graph()

# Додаємо користувачів (вершини) з випадковими віками
users = ["Анна", "Богдан", "Вікторія", "Дмитро", "Олена", 
         "Іван", "Катерина", "Марія", "Петро", "Софія"]

for user in users:
    G.add_node(user, age=random.randint(18, 40))

# Додаємо дружні зв'язки (ребра)
friendships = [
    ("Анна", "Богдан"), ("Анна", "Олена"), ("Богдан", "Дмитро"),
    ("Вікторія", "Олена"), ("Дмитро", "Іван"), ("Дмитро", "Петро"),
    ("Олена", "Софія"), ("Іван", "Катерина"), ("Катерина", "Марія"),
    ("Марія", "Петро"), ("Петро", "Софія"), ("Анна", "Вікторія"),
    ("Богдан", "Іван")
]

G.add_edges_from(friendships)

# Візуалізація
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)  # Фіксоване розташування

# Розфарбовуємо вершини за віком
colors = [G.nodes[user]['age'] for user in G.nodes()]
labels = {user: f"{user}\n({G.nodes[user]['age']} р.)" for user in G.nodes()}

nx.draw(G, pos, labels=labels, node_color=colors, cmap=plt.cm.YlOrRd, 
        node_size=1000, font_size=8, font_weight="bold", edge_color="gray")
plt.title("Соціальна мережа (колір = вік)")
plt.colorbar(plt.cm.ScalarMappable(cmap=plt.cm.YlOrRd), label="Вік")
plt.show()

# Аналіз
print("Аналіз соціальної мережі:")
print(f"- Кількість користувачів: {G.number_of_nodes()}")
print(f"- Кількість дружніх зв'язків: {G.number_of_edges()}")
print(f"- Середня кількість друзів: {sum(dict(G.degree()).values()) / G.number_of_nodes():.1f}")

# Найпопулярніший користувач (найбільше друзів)
most_popular = max(G.degree(), key=lambda x: x[1])
print(f"\nНайпопулярніший користувач: {most_popular[0]} ({most_popular[1]} друзів)")

# Ступінь кожної вершини
print("\nКількість друзів по кожному користувачу:")
for user, friends in sorted(G.degree(), key=lambda x: -x[1]):
    print(f"{user}: {friends} друзів")

# Список друзів для прикладу
print(f"\nДрузі Анни: {list(G.neighbors('Анна'))}")