import networkx as nx
from collections import deque
from task_1 import metro_graph_dict as g


def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end='\n')  # Відвідуємо вершину
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


def bfs(graph, start):
    # Ініціалізація порожньої множини для зберігання відвіданих вершин
    visited = set()
    # Ініціалізація черги з початковою вершиною
    queue = deque([start])

    while queue:  # Поки черга не порожня, продовжуємо обхід
        # Вилучаємо першу вершину з черги
        vertex = queue.popleft()
        # Перевіряємо, чи була вершина відвідана раніше
        if vertex not in visited:
            # Якщо не була відвідана, друкуємо її
            print(vertex, end="\n")
            # Додаємо вершину до множини відвіданих вершин
            visited.add(vertex)
            # Додаємо всіх невідвіданих сусідів вершини до кінця черги
            # Операція різниці множин вилучає вже відвідані вершини зі списку сусідів
            queue.extend(set(graph[vertex]) - visited)
    # Повертаємо множину відвіданих вершин після завершення обходу
    return visited


if __name__ == '__main__':
    # Створення графа (використовуючи код з першого завдання)
    G = nx.Graph(g)

    # Знаходження шляху за допомогою DFS
    print("DFS шлях:")
    dfs(G, 'Times Square')
    print("\n")

    # Знаходження шляху за допомогою BFS
    print("BFS шлях:")
    bfs(G, 'Times Square')
    print("\n")
