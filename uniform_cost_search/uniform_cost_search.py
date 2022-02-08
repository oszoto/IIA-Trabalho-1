from graph import *

def get_path_value(graph: WeightedGraph, path: list[str]) -> int:
  sum = 0
  cursor = 0
  while path[cursor] != path[-1]:
    neighbors = graph._connectionDict[path[cursor]]
    for neighbor in neighbors:
      if neighbor.value == path[cursor + 1]:
        sum += neighbor.weight
        break
    cursor += 1
  return sum

def get_cheapest_path(graph: WeightedGraph, paths: list[list[str]]) -> list[str]:
  cheapest = get_path_value(graph, paths[0])
  result = paths[0]
  for path in paths:
    v = get_path_value(graph, path)
    if v < cheapest:
       cheapest = v
       result = path
  return result

def get_cheapest_neighbor(neighbors = list[WeightedVertex], exclude = []) -> str:
  valid_neighbors = []
  for neighbor in neighbors:
    if exclude.count(neighbor.value) == 0:
      valid_neighbors.append(neighbor)
  if not valid_neighbors: 
    return 'EMPTY_NEIGHBORS'
  cheapest = valid_neighbors[0].weight
  result = valid_neighbors[0].value
  for neighbor in valid_neighbors:
    if neighbor.weight < cheapest:
      cheapest = neighbor.weight
      result = neighbor.value
  return result

def vertex_list_to_set(vertex_list: list[WeightedVertex]) -> list[str]:
  string_list = set()
  for vertex in vertex_list:
    string_list.add(vertex.value)
  return string_list

def uniform_cost_search(graph: WeightedGraph, start: str, end: str) -> list[str]:
  # initialization
  paths = []
  already_visited = [start]
  neighbors = graph.get_neighbors_of(start)
  for neighbor in neighbors:
    paths.append([start, neighbor.value])
    already_visited.append(neighbor.value)
  current_path = paths[0]
  current_vertex = current_path[-1]

  # running
  while current_vertex != end: 
    current_path = get_cheapest_path(graph, paths)
    current_vertex = current_path[-1]
    already_visited.append(current_vertex)
    neighbors = graph._connectionDict[current_vertex]
    next_vertex = get_cheapest_neighbor(neighbors, already_visited)
    if next_vertex == 'EMPTY_NEIGHBORS':
      paths.remove(current_path)
    else:
      paths.remove(current_path)
      valid_neighbors = list(vertex_list_to_set(neighbors) - set(already_visited))
      for neighbor in valid_neighbors:
        new_path = current_path.copy()
        new_path.append(neighbor)
        paths.append(new_path)

  return current_path

def main():
  map = WeightedGraph()
  map.populate_with_city_map()
  result = uniform_cost_search(map, 'Arad', 'Bucharest')
  print(result)

if __name__ == '__main__':
  main()