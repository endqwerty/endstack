-- 2024-01-02: integer cents replace the float dollar total.
ALTER TABLE orders ADD COLUMN total_cents INTEGER;
UPDATE orders SET total_cents = CAST(ROUND(legacy_total * 100) AS INTEGER)
  WHERE created_at >= '2024-01-01';
