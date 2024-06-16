from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
import duckdb

# Initialize Spark session with Kafka package
spark = SparkSession.builder \
    .appName("KafkaSparkDuckDB") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1") \
    .getOrCreate()

# Read from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "stock_data") \
    .load()

# Define schema and parse JSON
schema = "symbol STRING, timestamp STRING, open DOUBLE, high DOUBLE, low DOUBLE, close DOUBLE, volume DOUBLE"
parsed_df = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

# Write to DuckDB
def write_to_duckdb(batch_df, batch_id):
    # Connect to DuckDB, will create a new database file if not exists
    conn = duckdb.connect("stock_data.db")
    
    # Create table if it does not exist
    conn.execute("""
    CREATE TABLE IF NOT EXISTS stocks (
        symbol VARCHAR,
        timestamp TIMESTAMP,
        open DOUBLE,
        high DOUBLE,
        low DOUBLE,
        close DOUBLE,
        volume DOUBLE
    )
    """)
    
    # Append the new batch of data to the stocks table
    batch_df.toPandas().to_sql("stocks", conn, if_exists="append", index=False)

query = parsed_df.writeStream.foreachBatch(write_to_duckdb).start()
query.awaitTermination()
