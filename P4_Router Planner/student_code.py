from heapq import heappush, heappop # needed for Priority Queue
import math # needed for computing the distance

class PriorityQueue:
    
    def __init__(self, iterable = []):
        self.heap = []
        for value in iterable:
            heappush(self.heap,(0,value))
            
    def add(self, value, priority=0):
        heappush(self.heap, (priority, value))
        
    def pop(self):
        priority, value = heappop(self.heap)
        return value
    
    def __len__(self):
        return len(self.heap)
    
def reconstruct_path(starting_point, start, end):
    """
    Given the set of predecessors for each node on the map, an origin (start) and a destination (end)
    returns a path as we need to show from start to end.
  
    """
    reversed_path = [end]
    
    while end != start:
        end = starting_point[end]
        reversed_path.append(end)
        
    return list(reversed(reversed_path))

def distance(xy1, xy2):
    
    """
    Given the cartesian coordinates (x,y) of two points,
    returns the Euclidean distance
    
    """
    
    x1 = xy1[0]
    y1 = xy1[1]
    
    x2 = xy2[0]
    y2 = xy2[1]
    
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def shortest_path(M: object, start: int, goal: int) -> list:
    
    """
    Given a map, an origin (start) and a destination (goal),
    returns the shortest path based on A* algorithm.
    Reference: https://leetcode.com/problems/shortest-path-in-binary-matrix/discuss/313347/a-search-in-python
    """
    
    # dictionary of Map intersections coordinates (x,y)
    nodes_xy = M.intersections
    
    # destination coordinates
    goal_xy = nodes_xy[goal]
    
    # list of lists of adjacent nodes
    nodes_connections = M.roads
    
    # Set of integers to track the visited nodes in the search
    visited = set()
    
    # Dictionary to track the predecessors in the path
    start_from = dict()
    
    # initialize single nodes distance from the origin
    nodes_id = nodes_xy.keys()        
    distance_dict = {node_id: math.inf for node_id in nodes_id}
    distance_dict[start] = 0
    
    # create frontier to be expanded as a PriorityQueue and add the origin to the PriorityQueue
    frontier = PriorityQueue()
    frontier.add(start)
    
    # loop until all the nodes in the frontier have been explored
    while frontier:
        
        # retrieve the node with the minimum cost from frontier
        node = frontier.pop()
        
        # check if the node has been processed
        if node in visited:
            continue
            
        # if node equal to goal, end search
        if node == goal:
            return reconstruct_path(start_from, start, node)
        
        # mark the current node as visited
        visited.add(node)
        
        # check all possible neighbours and update the cost function
        
        node_xy = nodes_xy[node] # current node's coordinates
        
        for neighbour in nodes_connections[node]:
            
            neighbour_xy = nodes_xy[neighbour] # neighbor's coordinates
            
            # total distance travelled to reach the neighbour
            total_cost = distance_dict[node] + distance(node_xy, neighbour_xy)
            
            # estimated distance for the remaining distance to goal
            estimate_cost = distance(neighbour_xy, goal_xy)
            
            # estimated cost of the path from start to goal via neighbour's position 
            total_cost_neigh = total_cost + estimate_cost
            
            # Compare the total distance travelled to neighbour with the actual distance_dict
            if total_cost < distance_dict[neighbour]:
                
                # update neighbour's distance, precedessor. And add it to the Priority Queue
                distance_dict[neighbour] = total_cost
                start_from[neighbour] = node
                frontier.add(neighbour, priority = total_cost_neigh)
                
    # there is no solution, the graph may be not fully connected
    return None

