import psycopg2
from shapely.geometry import Point
from shapely.wkt import dumps

conn = psycopg2.connect(
    host="localhost", database="ruteo", user="postgres", password="123"
)

cursor = conn.cursor()

epicentro = Point(-72.898, -36.122)

epicentro_wkt = dumps(epicentro)

query = "SELECT id, ST_Distance(ST_GeomFromText(%s, 4326), the_geom) AS distancia FROM fibra_optica_detectada_vertices_pgr"

cursor.execute(query, (epicentro_wkt,))

resultados = cursor.fetchall()

# for resultado in resultados:
#     nodo_id, distancia = resultado
#     print(f"Nodo {nodo_id} tiene una distancia de {round(100*distancia, 3)} kilometros al epicentro.")  # Imprime el ID del nodo_id, distancia)

with open("../data/distance_epicenter_nodos.txt", "w") as f:
    for resultado in resultados:
        nodo_id, distancia = resultado
        f.write(f"{nodo_id},{round(100*distancia, 3)}\n")

cursor.close()
conn.close()
