def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances


if __name__ == '__main__':
    graph_weighted = {
        'Times Square': {'Grand Central': 5, 'Union Square': 2},
        'Grand Central': {'Times Square': 8, 'Penn Station': 8, 'Central Park West': 9},
        'Union Square': {'Times Square': 8, 'Columbus Circle': 10, 'Rockefeller Center': 10},
        'Penn Station': {'Grand Central': 1, 'Central Park West': 7, 'Bryant Park': 8},
        'Central Park West': {'Grand Central': 2, 'Penn Station': 6, 'Empire State': 3, 'Flatiron District': 10},
        'Columbus Circle': {'Union Square': 6, 'Rockefeller Center': 1, 'Bryant Park': 2},
        'Rockefeller Center': {'Union Square': 8, 'Columbus Circle': 9, 'Empire State': 6, 'Flatiron District': 5},
        'Bryant Park': {'Penn Station': 8, 'Columbus Circle': 8, 'Chelsea Market': 8, 'Greenwich Village': 6},
        'Empire State': {'Central Park West': 6, 'Rockefeller Center': 6, 'Flatiron District': 1, 'Chelsea Market': 4},
        'Flatiron District': {'Central Park West': 4, 'Rockefeller Center': 9, 'Empire State': 9, 'Chelsea Market': 7},
        'Chelsea Market': {'Bryant Park': 6, 'Empire State': 1, 'Greenwich Village': 7, 'Brooklyn Bridge': 9},
        'Greenwich Village': {'Bryant Park': 5, 'Flatiron District': 6, 'Brooklyn Bridge': 4},
        'Brooklyn Bridge': {'Chelsea Market': 5, 'Greenwich Village': 8, 'Wall Street': 5, 'Battery Park': 10},
        'Wall Street': {'Brooklyn Bridge': 6, 'Battery Park': 2, 'Staten Island Ferry': 9},
        'Battery Park': {'Brooklyn Bridge': 8, 'Wall Street': 8, 'Staten Island Ferry': 7},
        'Staten Island Ferry': {'Wall Street': 8, 'Battery Park': 4}, 'South Ferry': {'Wall Street': 10},
        'Whitehall Street': {'South Ferry': 5}, 'Bowling Green': {'Whitehall Street': 3},
        'Fulton Street': {'Bowling Green': 5, 'Wall Street': 5},
        'Chambers Street': {'Fulton Street': 6, 'Brooklyn Bridge': 2}, 'Brooklyn Bridge-City Hall': {'Chambers Street': 8},
        'Cortlandt Street': {'Chambers Street': 3, 'World Trade Center': 6},
        'World Trade Center': {'Cortlandt Street': 5, 'Fulton Street': 5, 'Battery Park': 8}
    }

    for vertex, neighbors in graph_weighted.items():
        print(f"{vertex}: {dijkstra(graph_weighted, vertex)}")
