import subprocess
from dagster import job, op, DagsterInstance, execute_job, reconstructable

@op
def produce_data_to_kafka(context):
    context.log.info("Producing data to Kafka")
    subprocess.run(["python", "producer.py"])

@op
def consume_data_from_kafka(context):
    context.log.info("Consuming data from Kafka")
    subprocess.run(["spark-submit", "--packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1", "consumer.py"])

@op
def run_dbt_transformations(context):
    context.log.info("Running dbt transformations")
    subprocess.run(["dbt", "run"])

@job
def stock_data_pipeline():
    produce_data_to_kafka()
    consume_data_from_kafka()
    run_dbt_transformations()

if __name__ == "__main__":
    instance = DagsterInstance.local_temp()
    result = execute_job(reconstructable(stock_data_pipeline), instance=instance)
    assert result.success
