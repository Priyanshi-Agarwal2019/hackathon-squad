import sys
import time
import random

def solve():
    # Use fast I/O
    input = sys.stdin.read().split()
    if not input: return
    
    N, M = int(input[0]), int(input[1])
    skills = list(map(int, input[2:N+2]))
    
    adj = [[] for _ in range(N)]
    ptr = N + 2
    for _ in range(M):
        u = int(input[ptr]) - 1
        v = int(input[ptr+1]) - 1
        adj[u].append(v)
        adj[v].append(u)
        ptr += 2

    # Heuristic: Weighted Degree (Skill / Degree)
    # This helps pick high-value nodes that block low-value neighbors
    order = sorted(range(N), key=lambda x: skills[x] / (len(adj[x]) + 1), reverse=True)
    
    selected = [False] * N
    current_score = 0
    
    # Fast Greedy Initial State
    for i in order:
        can_add = True
        for neighbor in adj[i]:
            if selected[neighbor]:
                can_add = False
                break
        if can_add:
            selected[i] = True
            current_score += skills[i]

    best_score = current_score
    best_set = selected[:]
    
    start_time = time.time()
    # Use ~4.5 minutes to be safe
    limit = 270 
    
    # Local Search with Perturbation
    # Instead of just picking random, we try to 'swap'
    while time.time() - start_time < limit:
        # Pick a node not in the set
        v = random.randrange(N)
        
        if not selected[v]:
            # Calculate what we lose by adding v
            conflicts = [nb for nb in adj[v] if selected[nb]]
            loss = sum(skills[nb] for nb in conflicts)
            
            # Simple thresholding: accept if it improves or is close (Metropolis-like)
            if skills[v] > loss:
                selected[v] = True
                for nb in conflicts:
                    selected[nb] = False
                current_score += (skills[v] - loss)
        else:
            # Occasionally drop a node to escape local optima
            if random.random() < 0.01:
                selected[v] = False
                current_score -= skills[v]

        if current_score > best_score:
            best_score = current_score
            best_set = selected[:]

    # Output
    print(best_score)
    result = [i + 1 for i, val in enumerate(best_set) if val]
    print(*(result))

if __name__ == "__main__":
    solve()
