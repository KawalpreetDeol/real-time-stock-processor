import duckdb

conn = duckdb.connect('stock_data.db')
result = conn.execute('SELECT * FROM stocks LIMIT 10').fetchall()
print(result)
