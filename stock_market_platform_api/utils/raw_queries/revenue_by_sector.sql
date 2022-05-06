SELECT
    sector,
    fiscal_period,
    SUM(value)
FROM (
    SELECT
        sector,
        CASE
            WHEN EXTRACT(MONTH FROM fiscal_period) <= 3 THEN MAKE_DATE(EXTRACT(YEAR FROM fiscal_period)::int, 3, 30)
            WHEN EXTRACT(MONTH FROM fiscal_period) <= 6 THEN MAKE_DATE(EXTRACT(YEAR FROM fiscal_period)::int, 6, 30)
            WHEN EXTRACT(MONTH FROM fiscal_period) <= 9 THEN MAKE_DATE(EXTRACT(YEAR FROM fiscal_period)::int, 9, 30)
            WHEN EXTRACT(MONTH FROM fiscal_period) <= 12 THEN MAKE_DATE(EXTRACT(YEAR FROM fiscal_period)::int, 12, 30)
        END AS fiscal_period,
        value
    FROM income_statements
    WHERE name = 'total_revenue') AS buckets
GROUP BY sector, fiscal_period
ORDER BY sector, fiscal_period;
