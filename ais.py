import numpy as np
import random

# Sample dataset: [feature1, feature2, class]
# class: 0 = Healthy, 1 = Damaged
data = np.array([
    [2.0, 3.0, 0],
    [2.5, 3.5, 0],
    [8.0, 7.0, 1],
    [7.5, 6.5, 1]
])

# Parameters
num_antibodies = 5
num_generations = 20
mutation_rate = 0.1

# Initialize antibodies randomly
def init_antibodies():
    return [np.random.rand(2) * 10 for _ in range(num_antibodies)]

# Affinity (inverse distance)
def affinity(ab, antigen):
    return 1 / (1 + np.linalg.norm(ab - antigen))

# Evaluate antibody (classification ability)
def evaluate(ab):
    score = 0
    for row in data:
        x = row[:2]
        label = row[2]
        
        dist = np.linalg.norm(ab - x)
        pred = 0 if dist < 3 else 1   # simple threshold
        
        if pred == label:
            score += 1
    return score

# Mutation
def mutate(ab):
    return ab + np.random.normal(0, mutation_rate, size=ab.shape)

# AIS Algorithm
antibodies = init_antibodies()

for _ in range(num_generations):
    # Evaluate
    scores = [(ab, evaluate(ab)) for ab in antibodies]
    
    # Select best
    scores.sort(key=lambda x: x[1], reverse=True)
    best = [ab for ab, _ in scores[:2]]
    
    # Clone and mutate
    new_antibodies = []
    for ab in best:
        for _ in range(2):  # cloning
            clone = mutate(ab)
            new_antibodies.append(clone)
    
    antibodies = best + new_antibodies

# Final best antibody
best_ab = max(antibodies, key=evaluate)
print("Best antibody (classifier):", best_ab)

# Test classification
test = np.array([7.0, 6.0])
dist = np.linalg.norm(best_ab - test)
prediction = "Damaged" if dist > 3 else "Healthy"

print("Test sample:", test)
print("Prediction:", prediction)