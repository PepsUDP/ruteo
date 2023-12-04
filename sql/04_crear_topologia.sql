-- Agregar columnas "source" y "target" para crear la topología
BEGIN;

ALTER TABLE IF EXISTS fibra_optica_detectada
ADD COLUMN IF NOT EXISTS "source" integer,
ADD COLUMN IF NOT EXISTS "target" integer;

COMMIT;

-- Crear la topología con tolerancia de 0.00001
BEGIN;

SELECT
    pgr_createTopology ('fibra_optica_detectada', 0.00001, 'geom', 'gid');

COMMIT;