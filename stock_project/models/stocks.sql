-- models/stocks.sql
SELECT
    symbol,
    CAST(timestamp AS TIMESTAMP) AS event_time,
    open,
    high,
    low,
    close,
    volume
FROM
    {{ ref('raw_stocks') }}
