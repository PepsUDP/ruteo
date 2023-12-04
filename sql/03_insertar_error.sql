-- Añadir columnas de probabilidad de fallo (error_prob)
BEGIN;

ALTER TABLE IF EXISTS fibra_optica_detectada
ADD COLUMN IF NOT EXISTS "error_prob" FLOAT DEFAULT 0.0 NOT NULL;

COMMIT;