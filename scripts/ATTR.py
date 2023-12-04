import numpy as np

with open("../data/adjacency_matrix.txt", "r") as f:
    adjacency_matrix = np.loadtxt(f, delimiter=",", dtype=int)

n = len(adjacency_matrix)

# Revisar si hay conexiones en la diagonal (mismo nodo)
for i in range(n):
    for j in range(n):
        if i == j:
            if adjacency_matrix[i][j] != 0:
                print("Hay una conexión en la diagonal:", i, j)

# Total de Conexiones
z = adjacency_matrix.sum()
print(z)

ATTR = pow((2078 * 2079) / 2, -1) * z
print(ATTR)
