import numpy as np
import random

# Distance matrix (example)
dist = np.array([
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
])

n = len(dist)

# Parameters
num_ants = 5
num_iterations = 50
alpha = 1      # pheromone importance
beta = 2       # distance importance
evaporation = 0.5
Q = 100

# Initialize pheromone
pheromone = np.ones((n, n))


def route_length(route):
    total = 0
    for i in range(len(route)-1):
        total += dist[route[i]][route[i+1]]
    total += dist[route[-1]][route[0]]  # return to start
    return total


def choose_next_city(current, unvisited):
    probs = []
    for city in unvisited:
        tau = pheromone[current][city] ** alpha
        eta = (1 / dist[current][city]) ** beta
        probs.append(tau * eta)
    
    probs = probs / np.sum(probs)
    return random.choices(unvisited, weights=probs)[0]


best_route = None
best_length = float('inf')

for _ in range(num_iterations):
    all_routes = []
    
    for _ in range(num_ants):
        start = random.randint(0, n-1)
        route = [start]
        unvisited = list(range(n))
        unvisited.remove(start)
        
        current = start
        while unvisited:
            next_city = choose_next_city(current, unvisited)
            route.append(next_city)
            unvisited.remove(next_city)
            current = next_city
        
        all_routes.append(route)
        
        length = route_length(route)
        if length < best_length:
            best_length = length
            best_route = route
    
    # Evaporation
    pheromone *= (1 - evaporation)
    
    # Update pheromone
    for route in all_routes:
        length = route_length(route)
        for i in range(len(route)-1):
            pheromone[route[i]][route[i+1]] += Q / length

print("Best Route:", best_route)
print("Shortest Distance:", best_length)