# Real-Time Stock Processor

## Project Overview
The Real-Time Stock Processor is a comprehensive project that demonstrates the integration of various data technologies to process real-time stock data. The project ingests stock data from Yahoo Finance, processes and stores it using Kafka and PySpark, saves the processed data in DuckDB, transforms the data using dbt, and orchestrates the entire workflow with Dagster.

## Technologies Used
- Python
- Apache Kafka
- PySpark
- DuckDB
- dbt
- Dagster
- Yahoo Finance (yfinance library)

## Project Components
### Data Ingestion
- Source: The project starts by fetching real-time stock data from Yahoo Finance using the yfinance library.
- Kafka: This data is sent to an Apache Kafka topic (stock_data). Kafka acts as a distributed streaming platform, buffering and streaming the data for further processing.

### Data Processing
- PySpark: The consumer.py script reads data from the Kafka topic using PySpark. PySpark's structured streaming API enables real-time data processing.
- Transformation: The data is parsed, transformed, and cleaned within the PySpark streaming job.

### Data Storage
- DuckDB: Processed data is stored in DuckDB, an in-process SQL OLAP database management system. DuckDB is chosen for its simplicity and ease of integration, making it suitable for this project.

### Data Transformation
- dbt: The project utilizes dbt (data build tool) to transform the raw data stored in DuckDB. dbt helps define and run SQL transformations, producing clean and well-organized data models.

### Workflow Orchestration
- Dagster: Dagster is used to orchestrate the entire workflow. It manages the sequence and dependencies of various steps, ensuring smooth data flow from ingestion to final transformation.

## Detailed Workflow
1. Producer (Data Ingestion):
    - The `producer.py` script fetches stock data from Yahoo Finance for a specified stock symbol (e.g., AAPL).
    - This data is serialized into JSON and sent to the Kafka topic stock_data.

2. Consumer (Data Processing and Storage):
    - The `consumer.py` script reads data from the Kafka topic using PySpark.
    - It parses the JSON data, processes it, and writes it to a DuckDB database file (stock_data.db).

3. dbt (Data Transformation):
    - dbt runs SQL models to transform the raw data in DuckDB.
    - Models such as `raw_stocks.sql`, `stocks.sql`, and `daily_aggregates.sql` define the transformations and aggregations.

4. Dagster (Workflow Orchestration):
    - The `pipeline.py` script defines a Dagster job with three operations: `produce_data_to_kafka`, `consume_data_from_kafka`, and `run_dbt_transformations`.
    - Dagster executes these operations in sequence, ensuring each step completes before the next begins.


## Setup Instructions

### Prerequisites
- Python 3.6 or higher
- Java JDK 17 or higher
- Git
- Anaconda (recommended)
    - Pip and Virtual env built-in

### Step 1: Set Up Environment Variables

1. **JAVA_HOME**: Set to the JDK installation path (e.g., `C:\Program Files\Java\jdk-22`)
2. **HADOOP_HOME**: Set to the Hadoop installation path (e.g., `C:\hadoop`)
3. **SPARK_HOME**: Set to the Spark installation path (e.g., `C:\spark`)
4. **Path**: Add the following paths to the `Path` variable:
   ```sh
   %JAVA_HOME%\bin
   %HADOOP_HOME%\bin
   %SPARK_HOME%\bin
   C:\Users\YourUsername\anaconda3
   C:\Users\YourUsername\anaconda3\Scripts

### Step 2: Install Required Software
#### Install Java Development Kit (JDK)

Download and install the latest JDK from Oracle JDK download page or OpenJDK page.
Install Hadoop (for Winutils)

#### Install Hadoop (for Winutils)
Download Hadoop from the Hadoop Releases page.
Extract the Hadoop tar.gz file to a directory (e.g., `C:\hadoop`).
Download winutils.exe for the version of Hadoop from here and place it in `C:\hadoop\bin`.
Install Spark

#### Install Spark
Download Spark from the Apache Spark download page.
Choose Spark 3.5.1, and select the package type with Hadoop included.
Extract Spark to a directory (e.g., `C:\spark`).

#### Install Kafka
Download Kafka from the Apache Kafka download page.
Choose the latest binary for your operating systems.
Extract the downloaded Kafka files to a directory (e.g. `C:\kafka`)

### Step 3: Intall Python Packages
1. Create and Activate Conda Environment
    ```sh
    conda create --name stock_processor python=3.8
    conda activate stock_processor

2. Install Required Python Packages
    ```sh
    pip install yfinance kafka-python pyspark duckdb dbt-duckdb dagster

3. Set Environment Variables for PySpark
    ``` sh
    mkdir -p $CONDA_PREFIX/etc/conda/activate.d
    echo 'export PYSPARK_PYTHON=$(which python)' > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
    echo 'export PYSPARK_DRIVER_PYTHON=$(which python)' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh

4. Set Up Kafka
In your Kafka folder, run the following commands (for windows):
    1. Start Zookeeper
        ```sh
        bin/windows/zookeeper-server-start.bat config/zookeeper.properties

    2. Start Kafka Server
        ```sh
        bin/windows/kafka-server-start.bat config/server.properties

    3. Create Kafka Topic
        ```sh
        bin/windows/kafka-topics.bat --create --topic stock_data --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

## Running the Project
### Step 5: Produce Real-Time Stock Data to Kafka
- Run the producer script:
    ```sh
    python producer.py

### Step 6: Consume Data from Kafka Using PySpark
- Run the consumer script: 
    ```sh
    spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 consumer.py

### Step 7: Run dbt Models
- A dbt project should be created along with this project. Simply do:
    ```sh
    dbt run

### Step 8: Orchestrate the Workflow with Dagster
- Run the Dagster Pipeline:
    ```sh
    Run pipeline.py

### Step 9: Check if the Pipeline Excuted Successfully
- Run the duckdb check script:
    ```sh
    python duckdb_check.py > results.txt
A results.txt file will be created will all of the data stored in duckdb.







