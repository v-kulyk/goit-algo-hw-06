import networkx as nx
import matplotlib.pyplot as plt

metro_graph_dict = {
    'Times Square': ['Grand Central', 'Union Square'],
    'Grand Central': ['Times Square', 'Penn Station', 'Central Park West'],
    'Union Square': ['Times Square', 'Columbus Circle', 'Rockefeller Center'],
    'Penn Station': ['Grand Central', 'Central Park West', 'Bryant Park'],
    'Central Park West': ['Grand Central', 'Penn Station', 'Empire State', 'Flatiron District'],
    'Columbus Circle': ['Union Square', 'Rockefeller Center', 'Bryant Park'],
    'Rockefeller Center': ['Union Square', 'Columbus Circle', 'Empire State', 'Flatiron District'],
    'Bryant Park': ['Penn Station', 'Columbus Circle', 'Chelsea Market', 'Greenwich Village'],
    'Empire State': ['Central Park West', 'Rockefeller Center', 'Flatiron District', 'Chelsea Market'],
    'Flatiron District': ['Central Park West', 'Rockefeller Center', 'Empire State', 'Chelsea Market'],
    'Chelsea Market': ['Bryant Park', 'Empire State', 'Greenwich Village', 'Brooklyn Bridge'],
    'Greenwich Village': ['Bryant Park', 'Flatiron District', 'Brooklyn Bridge'],
    'Brooklyn Bridge': ['Chelsea Market', 'Greenwich Village', 'Wall Street', 'Battery Park'],
    'Wall Street': ['Brooklyn Bridge', 'Battery Park', 'Staten Island Ferry'],
    'Battery Park': ['Brooklyn Bridge', 'Wall Street', 'Staten Island Ferry'],
    'Staten Island Ferry': ['Wall Street', 'Battery Park'],
    'South Ferry': ['Wall Street'],
    'Whitehall Street': ['South Ferry'],
    'Bowling Green': ['Whitehall Street'],
    'Fulton Street': ['Bowling Green', 'Wall Street'],
    'Chambers Street': ['Fulton Street', 'Brooklyn Bridge'],
    'Brooklyn Bridge-City Hall': ['Chambers Street'],
    'Cortlandt Street': ['Chambers Street', 'World Trade Center'],
    'World Trade Center': ['Cortlandt Street', 'Fulton Street', 'Battery Park']
}

if __name__ == '__main__':
    # Створення графа
    G = nx.Graph(metro_graph_dict)

    # Аналіз основних характеристик графа
    print("Кількість вершин:", G.number_of_nodes())
    print("Кількість ребер:", G.number_of_edges())
    print("Список вершин:", list(G.nodes()))
    print("Список ребер:", list(G.edges()))
    print("Ступінь вершин:", dict(G.degree()))

    # Вивід графа
    nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
    plt.show()



