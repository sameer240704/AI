import numpy as np

class AntColony:
    def __init__(self, num_cities, num_ants, alpha=1, beta=2, evaporation_rate=0.5, pheromone_init=0.1):
        self.num_cities = num_cities
        self.num_ants = num_ants
        self.alpha = alpha  # Pheromone influence factor
        self.beta = beta    # Heuristic influence factor
        self.evaporation_rate = evaporation_rate
        self.pheromone_init = pheromone_init
        self.pheromones = np.ones((num_cities, num_cities)) * pheromone_init
        self.distances = np.zeros((num_cities, num_cities))  # Distance matrix
        self.ants = np.zeros((num_ants, num_cities), dtype=int)  # Ants memory
        self.path_costs = np.zeros(num_ants)  # Path cost for each ant

    def add_distances(self, distances):
        self.distances = distances

    def run(self, num_iterations):
        best_path = None
        best_cost = float('inf')
        for iteration in range(num_iterations):
            all_paths = []
            print(f"\nIteration {iteration + 1}")
            for ant in range(self.num_ants):
                ant_path, path_cost = self.ant_tour(ant)
                all_paths.append((ant_path, path_cost))
                print(f"Ant {ant}: Path: {ant_path}, Cost: {path_cost}")
                if path_cost < best_cost:
                    best_cost = path_cost
                    best_path = ant_path
            self.update_pheromones(all_paths)
        return best_path, best_cost

    def ant_tour(self, ant):
        ant_path = np.zeros(self.num_cities, dtype=int)
        visited_cities = np.zeros(self.num_cities, dtype=bool)
        current_city = np.random.randint(0, self.num_cities)
        visited_cities[current_city] = True
        ant_path[0] = current_city
        path_cost = 0
        for i in range(1, self.num_cities):
            probabilities = self.get_probabilities(visited_cities, current_city)
            next_city = np.random.choice(np.arange(self.num_cities), p=probabilities)
            ant_path[i] = next_city
            visited_cities[next_city] = True
            path_cost += self.distances[current_city, next_city]
            current_city = next_city
        path_cost += self.distances[current_city, ant_path[0]]  # Return to starting city
        return ant_path, path_cost

    def get_probabilities(self, visited_cities, current_city):
        pheromone = np.copy(self.pheromones[current_city])
        pheromone[visited_cities] = 0
        distances_inv = 1 / (self.distances[current_city] + 1e-10)  # Avoid division by zero
        heuristic = distances_inv ** self.beta
        probabilities = (pheromone ** self.alpha) * heuristic
        probabilities /= np.sum(probabilities)
        return probabilities

    def update_pheromones(self, all_paths):
        self.pheromones *= (1 - self.evaporation_rate)
        for ant_path, path_cost in all_paths:
            for i in range(self.num_cities - 1):
                city_from, city_to = ant_path[i], ant_path[i + 1]
                self.pheromones[city_from, city_to] += 1 / (path_cost + 1e-10)  # Avoid division by zero
            self.pheromones[ant_path[-1], ant_path[0]] += 1 / (path_cost + 1e-10)  # Return to starting city

# Example usage
num_cities = int(input("Enter the number of cities: "))
num_ants = int(input("Enter the number of ants: "))
aco = AntColony(num_cities=num_cities, num_ants=num_ants)

# Input distances between cities
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[i][j] = float(input(f"Enter distance between city {i} and {j}: "))

aco.add_distances(distances)
num_iterations = int(input("Enter the number of iterations: "))
best_path, best_cost = aco.run(num_iterations)

print("\nBest path:", best_path)
print("Best cost:", best_cost)