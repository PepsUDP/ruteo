import psycopg2
from shapely.geometry import Point
from shapely.wkb import loads

conn = psycopg2.connect(
    host="localhost", database="ruteo", user="postgres", password="123"
)

cursor = conn.cursor()

epicentro = Point(-72.898, -36.122)

# epicentro_wkt = dumps(epicentro)

query = "SELECT gid, geom FROM fibra_optica_detectada"
cursor.execute(query)

resultados = cursor.fetchall()

with open("../data/distance_epicenter_aristas.txt", "w") as f:
    for resultado in resultados:
        arista_id, arista_geom_wkb = resultado
        arista_geom = loads(arista_geom_wkb, hex=True)
        distancia = arista_geom.distance(epicentro)
        f.write(f"{arista_id},{round(100*distancia, 3)}\n")

cursor.close()
conn.close()
