class WeightedVertex:
  def __init__(self, value: str, weight: int):
    self.value = value
    self.weight = weight
  def __repr__(self):
    return '(' + str(self.value) + '; ' + str(self.weight) + ')'

class WeightedGraph:
  def __init__(self):
    self._connectionDict = {}
  
  def insert(self, vertex: str, connections: list[WeightedVertex]) -> None:
    self._connectionDict.update({vertex: connections})

  def get_neighbors_of(self, identifier: str) -> list[WeightedVertex]:
    return self._connectionDict[identifier]

  def get_neighbor(self, vertex: str, neighbor: str) -> WeightedVertex:
    neighbor_list = self._connectionDict[vertex]
    for item in neighbor_list:
      if item.value == neighbor:
        return item
    raise KeyError(neighbor)

  # Fills this graph with the map specific to the class project
  def populate_with_city_map(self):
    self._connectionDict = {
      'Arad': [WeightedVertex('Zerind', 75), WeightedVertex('Sibiu', 140), WeightedVertex('Timisoara', 118)],
      'Bucharest': [WeightedVertex('Fagaras', 211), WeightedVertex('Pitesti', 101)],
      'Craiova': [WeightedVertex('Pitesti', 138), WeightedVertex('Rimnicu Vilcea', 146), WeightedVertex('Dobreta', 120)],
      'Dobreta': [WeightedVertex('Mehadia', 75), WeightedVertex('Craiova', 120)],
      'Fagaras': [WeightedVertex('Bucharest', 211), WeightedVertex('Sibiu', 99)],
      'Lugoj': [WeightedVertex('Timisoara', 111), WeightedVertex('Mehadia', 70)],
      'Mehadia': [WeightedVertex('Lugoj', 70), WeightedVertex('Dobreta', 75)],
      'Oradea': [WeightedVertex('Zerind', 71), WeightedVertex('Sibiu', 151)],
      'Pitesti': [WeightedVertex('Rimnicu Vilcea', 97), WeightedVertex('Bucharest', 101), WeightedVertex('Craiova', 138)],
      'Rimnicu Vilcea': [WeightedVertex('Pitesti', 97), WeightedVertex('Sibiu', 80), WeightedVertex('Craiova', 146)],
      'Sibiu': [WeightedVertex('Arad', 140), WeightedVertex('Fagaras', 99), WeightedVertex('Rimnicu Vilcea', 80)],
      'Timisoara': [WeightedVertex('Arad', 118), WeightedVertex('Lugoj', 111)],
      'Zerind': [WeightedVertex('Oradea', 71), WeightedVertex('Arad', 75)]
      }