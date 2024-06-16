-- models/daily_aggregates.sql
SELECT
    symbol,
    DATE(event_time) AS date,
    MAX(high) AS high,
    MIN(low) AS low,
    SUM(volume) AS total_volume
FROM
    {{ ref('stocks') }}
GROUP BY
    symbol, date
