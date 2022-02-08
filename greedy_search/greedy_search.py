from graph import WeightedGraph

def greedy_search(graph: WeightedGraph, distances: dict[str, int], 
  start: str, end: str = 'Bucharest') -> list[str]:

  #initializing
  current_vertex = start
  current_path = [start]

  #running
  while current_vertex != end:
    neighbors = graph.get_neighbors_of(current_vertex)
  
    smallest = neighbors[0]
    for neighbor in neighbors:
      if distances[neighbor.value] < distances[smallest.value]: 
        smallest = neighbor
    current_path.append(smallest.value)
    current_vertex = smallest.value

  return current_path


def main():

  #define heuristic information
  straight_distance_to_bucharest = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Dobreta': 242,
    'Fagaras': 178,
    'Lugoj': 244,
    'Mehadia': 241,
    'Oradea': 380,
    'Pitesti': 98,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Zerind': 374
  }

  map = WeightedGraph()
  map.populate_with_city_map()

  search_result = greedy_search(map, straight_distance_to_bucharest, 'Arad')
  print(search_result)

  return 0

if __name__ == '__main__':
  main()