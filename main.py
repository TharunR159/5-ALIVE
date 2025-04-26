import math
import itertools

def read_waypoints(filename):
    """Read waypoints from file with ID and 3D coordinates"""
    ids = []
    coords = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split()
            ids.append(int(parts[0]))  # First part is ID
            coords.append(tuple(map(float, parts[1:])))  # Next three parts are x, y, z
    return ids, coords

def euclidean_3d(p1, p2):
    """Calculate 3D Euclidean distance"""
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

def build_distance_matrix(waypoints):
    """Create N x N distance matrix"""
    n = len(waypoints)
    return [[euclidean_3d(waypoints[i], waypoints[j]) for j in range(n)] for i in range(n)]

def tsp_brute_force(dist_matrix):
    """Optimal TSP solution using brute-force"""
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

def main():
    try:
        ids, waypoints = read_waypoints('waypoints.txt')
        dist_matrix = build_distance_matrix(waypoints)

        path, cost = tsp_brute_force(dist_matrix)  # <= we only have 9 cities

        # Convert indices to real IDs
        output_path = [ids[i] for i in path]
        output_line = " ".join(str(i) for i in output_path) + f" {cost:.2f}"

        with open('path.txt', 'w') as f:
            f.write(output_line + "\n")

        print(output_line)

    except FileNotFoundError:
        print("Error: 'waypoints.txt' not found")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    main()
