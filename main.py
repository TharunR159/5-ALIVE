import math
import itertools

def read_waypoints(filename):
    """Read 3D coordinates from file without IDs"""
    with open(filename, 'r') as f:
        coords = []
        for line in f:
            parts = line.strip().split()
            coords.append(tuple(map(float, parts)))  # Convert all parts to floats
        return list(range(len(coords))), coords  # Generate IDs as indices

def euclidean_3d(p1, p2):
    """Calculate 3D Euclidean distance"""
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

def build_distance_matrix(waypoints):
    """Create N x N distance matrix"""
    n = len(waypoints)
    dist_matrix = [[euclidean_3d(waypoints[i], waypoints[j]) for j in range(n)] for i in range(n)]
    return dist_matrix

def tsp_brute_force(dist_matrix):
    """Optimal TSP solution using brute-force search"""
    n = len(dist_matrix)
    min_cost = float('inf')
    best_path = []
    
    for perm in itertools.permutations(range(1, n)):
        cost = dist_matrix[0][perm[0]]
        cost += sum(dist_matrix[perm[i]][perm[i + 1]] for i in range(len(perm) - 1))
        cost += dist_matrix[perm[-1]][0]
        
        if cost < min_cost:
            min_cost = cost
            best_path = [0] + list(perm) + [0]
    
    return best_path, min_cost

def tsp_nearest_neighbor(dist_matrix):
    """Heuristic TSP solution using nearest neighbor"""
    n = len(dist_matrix)
    visited = [False] * n
    path = [0]
    visited[0] = True
    current = 0
    
    for _ in range(n - 1):
        next_city = min((j for j in range(n) if not visited[j]), key=lambda j: dist_matrix[current][j])
        path.append(next_city)
        visited[next_city] = True
        current = next_city
    
    path.append(0)
    cost = sum(dist_matrix[path[i]][path[i + 1]] for i in range(n))
    return path, cost

def improve_solution(path, cost, dist_matrix):
    """Improve TSP solution using 2-opt optimization"""
    improved = True
    n = len(path) - 1
    
    while improved:
        improved = False
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                new_path = path[:i] + path[i:j + 1][::-1] + path[j + 1:]
                new_cost = sum(dist_matrix[new_path[k]][new_path[k + 1]] for k in range(n))
                if new_cost < cost:
                    path, cost = new_path, new_cost
                    improved = True
    return path, cost

def main():
    try:
        ids, waypoints = read_waypoints('waypoints.txt')
        dist_matrix = build_distance_matrix(waypoints)
        
        if len(waypoints) <= 10:
            path, cost = tsp_brute_force(dist_matrix)
        else:
            path, cost = tsp_nearest_neighbor(dist_matrix)
            path, cost = improve_solution(path, cost, dist_matrix)

        # ✅ Convert to 1-based indexing for output
        output_line = " ".join(str(ids[i] + 1) for i in path) + f" {cost:.2f}"

        with open('path.txt', 'w') as f:
            f.write(output_line + "\n")

        print(output_line)

    except FileNotFoundError:
        print("Error: 'waypoints.txt' not found")
    except Exception as e:
        print(f"Error: {str(e)}")

if _name_ == '_main_':
    main()
