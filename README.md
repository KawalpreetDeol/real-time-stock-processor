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







