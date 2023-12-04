# Crear tabla con datos de fibra óptica detectada
shp2pgsql -D -I -s 4326 ./recursos/fibra_optica_detectada.shp fibra_optica_detectada | psql dbname=ruteo postgres host=localhost
