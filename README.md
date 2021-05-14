# Data-Engineering-Nanodegree-Projects
Projects for Udacity Data Engineering Nanodegree Program
## Summary
Learn to design data models, build data warehouses and data lakes, automate data pipelines, and work with massive datasets. Projects are all based on a virtual music streaming company called Sparkify. 

 - Create user-friendly relational and NoSQL data models 
 - Create scalable and efficient data warehouses 
 - Work efficiently with massive datasets 
 -  Build and interact with a cloud-based data lake 
 - Automate and monitor data pipelines 
 - Develop proficiency in Spark, Airflow, and AWS tools
 
#### Techniques: SQL, Python, AWS, Spark, Airflow
---
## Project 1 Data Modeling with Postgres
### Overview
Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. They asked data engineers to create a Postgres database with tables designed to optimize queries on song play analysis, which could make them query the data easier.  The project is to create a database schema and ETL pipeline for this analysis.

 - Create Tables in `sql_queries.py` to create each table. 
 - Run  `create_tables.py`  to create database and tables.
 - Build ETL Processes  in `etl.ipynb` notebook to develop ETL processes for each table. Run `test.ipynb` to confirm that records were successfully inserted into each table.
 - Build ETL Pipeline. Use `etl.ipynb` to complete `etl.py` to process the entire datasets.
---
## Project 2 Data Modeling with Apache Cassandra

### Overview
Model user activity data for a music streaming app called Sparkify. Create a database and ETL
pipeline, in both Postgres and Apache Cassandra, designed to optimize queries for understanding what songs users are listening to. 

 - Process the `event_datafile_new.csv` dataset to create a denormalized dataset
 - Design tables to answer the queries outlined in the project sheet
 - Load the data into tables created in Apache Cassandra and run queries
 
 ---
 ## Project 3 Data Warehouse 
### Overview
Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app.  
Data engineers are tasked with building an ETL pipeline that extracts their music data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to.

 - **Design schemas for fact and dimension tables.** Write a SQL  `CREATE`  statement for each of these tables in  `sql_queries.py`
 - **Launch a redshift cluster and create an IAM role** that has read access to S3. Add redshift database and IAM role info to  `dwh.cfg`.
 - **Build ETL Pipeline.** Implement the logic in  `etl.py`  to load data from S3 to staging tables on Redshift.  Implement the logic in  `etl.py`  to load data from staging tables to analytics tables on Redshift.
 
 ---
 ## Project 4 Data Lake with Spark
 
### Overview
Sparkify has grown their user base and song database even more and want to move their data warehouse to a data lake. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

Data Engineer are tasked with building an **ETL pipeline** that extracts their data from S3, processes them using Spark, and loads the data back into S3 as a set of dimensional tables. This will allow analytics team to continue finding insights in what songs their users are listening to.

- Load data from S3,  `dl.cfg`contains AWS credentials.
 - Write in  `etl.py`  to read data from S3. Processes that data using Spark to create Fact table and Dimension tables.
 - Write the data back to S3.
---
## Project 5 Data Pipelines with Airflow

### Overview
Work on the music streaming company’s data infrastructure by creating and automating a set of
data pipelines. Configure and schedule data pipelines with Airflow and monitor and debug production pipelines. Create custom operators to perform tasks such as staging the data, filling the data warehouse, and running checks on the data as the final step.

 - Configuring the DAG with correct task dependencies
 - Building the operators: Stage Operator, Fact and Dimension Operators, Data Quality Operator
 ![enter image description here](https://video.udacity-data.com/topher/2019/January/5c48ba31_example-dag/example-dag.png)


Reference: [Udacity Data Engineer Nanodegree](https://d20vrrgs8k4bvw.cloudfront.net/documents/en-US/Data+Engineering+Nanodegree+Program+Syllabus.pdf)
