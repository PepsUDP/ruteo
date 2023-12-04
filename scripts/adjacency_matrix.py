import pandas as pd
import numpy as np
import psycopg2

conn = psycopg2.connect(
    host="localhost", database="ruteo", user="postgres", password="123"
)

# Consulta SQL para obtener las columnas "source" y "target" de la tabla "fibra_optica_detectada"
query = "SELECT source, target FROM fibra_optica_detectada"

# Leer los datos de PostgreSQL en un DataFrame de Pandas
df = pd.read_sql(query, conn).sort_values(by="source")

# Cerrar la conexión a la base de datos
conn.close()

print(df.head())

# Obtener la lista única de nodos
nodes = np.unique(df[["source", "target"]])
print(nodes.shape)

# Crear la matriz de adyacencia inicializada con ceros
adjacency_matrix = np.zeros((len(nodes), len(nodes)), dtype=int)

# Llenar la matriz de adyacencia con 1 en las posiciones correspondientes
for index, row in df.iterrows():
    source_index = np.where(nodes == row["source"])[0][0]
    target_index = np.where(nodes == row["target"])[0][0]
    adjacency_matrix[source_index, target_index] = 1

np.savetxt("../data/adjacency_matrix.txt", adjacency_matrix, delimiter=",", fmt="%d")
