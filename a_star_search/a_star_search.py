from graph import *

LAST_ITEM = -1
FIRST_ITEM = 0

def measure_path(graph: WeightedGraph, path: list[str],
   distances: dict[str, int]):
  
  sum = 0
  for index, city in enumerate(path):
    if path[index] == path[LAST_ITEM]:
      sum += distances[city]
    else:
      sum += graph.get_neighbor(city, path[index + 1]).weight

  return sum

def get_cheapest_path(graph: WeightedGraph, paths: list[list[str]], 
  distances: dict[str, int]) -> list[str]:

  cheapest = measure_path(graph, paths[FIRST_ITEM], distances)
  result = paths[FIRST_ITEM]

  for path in paths:
    path_size = measure_path(graph, path, distances)
    if path_size < cheapest: 
      result = path
      cheapest = path_size

  return result

def a_star_search(graph: WeightedGraph, distances: dict[str, int],
  start: str, end: str = 'Bucharest') -> list[str]:

  #initialize
  current_city = start
  current_neighbors = graph.get_neighbors_of(start)
  paths = []
  already_visited = [start]
  for neighbor in current_neighbors:
    paths.append([start, neighbor.value])
  current_path = get_cheapest_path(graph, paths, distances)

  #running
  while current_city != end:
    current_path = get_cheapest_path(graph, paths, distances)
    paths.remove(current_path)
    current_city = current_path[LAST_ITEM]
    already_visited.append(current_city)
    current_neighbors = graph.get_neighbors_of(current_city)
    if not current_neighbors: continue

    for neighbor in current_neighbors:
      if already_visited.count(neighbor.value): 
        continue
      else:
        new_path = current_path.copy()
        new_path.append(neighbor.value)
        paths.append(new_path)

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
  result = a_star_search(map, straight_distance_to_bucharest, 'Arad')
  print(result)

if __name__ == '__main__':
  main()