import numpy as np
from numpy.linalg import norm

# Define two vectors
A = np.array([2, 1, 2, 3, 2, 9])
B = np.array([3, 4, 2, 4, 5, 5])

print("Vector A:", A)
print("Vector B:", B)

# Compute the dot product
dot_product = np.dot(A, B)

# Compute the L2 norms (magnitudes) of A and B
norm_A = norm(A)
norm_B = norm(B)

# Compute Cosine Similarity
cosine_similarity = dot_product / (norm_A * norm_B)

# Display the result
print("Cosine Similarity:", cosine_similarity)
