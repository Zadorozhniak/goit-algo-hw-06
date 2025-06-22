import heapq

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, name):
        self.vertices[name] = {}
    
    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self.vertices:
            self.add_vertex(from_vertex)
        if to_vertex not in self.vertices:
            self.add_vertex(to_vertex)
        self.vertices[from_vertex][to_vertex] = weight
        # Для неорієнтованого графу додамо зворотний зв'язок
        self.vertices[to_vertex][from_vertex] = weight
    
    def dijkstra(self, start_vertex):
        # Ініціалізація відстаней: початкова вершина - 0, інші - нескінченність
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start_vertex] = 0
        
        # Пріоритетна черга для зберігання вершин і їх поточних відстаней
        priority_queue = [(0, start_vertex)]
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            # Якщо знайдена відстань більша за записану, пропускаємо
            if current_distance > distances[current_vertex]:
                continue
                
            # Оновлюємо відстань до кожного сусіда
            for neighbor, weight in self.vertices[current_vertex].items():
                distance = current_distance + weight
                
                # Якщо знайдено коротший шлях
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances
    
    def find_all_shortest_paths(self):
        shortest_paths = {}
        for vertex in self.vertices:
            shortest_paths[vertex] = self.dijkstra(vertex)
        return shortest_paths

# Приклад використання
if __name__ == "__main__":
    # Створення графу
    graph = Graph()
    
    # Додавання вершин і ребер з вагами
    graph.add_edge('A', 'B', 4)
    graph.add_edge('A', 'C', 2)
    graph.add_edge('B', 'C', 1)
    graph.add_edge('B', 'D', 5)
    graph.add_edge('C', 'D', 8)
    graph.add_edge('C', 'E', 10)
    graph.add_edge('D', 'E', 2)
    graph.add_edge('D', 'F', 6)
    graph.add_edge('E', 'F', 2)
    
    # Знаходження найкоротших шляхів від кожної вершини до всіх інших
    all_shortest_paths = graph.find_all_shortest_paths()
    
    # Вивід результатів
    for start_vertex in all_shortest_paths:
        print(f"Найкоротші шляхи від вершини {start_vertex}:")
        for end_vertex, distance in all_shortest_paths[start_vertex].items():
            print(f"  до {end_vertex}: {distance}")
        print()