## Data Modeling with Postgres

### Summary

Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. They asked data engineers to create a Postgres database with tables designed to optimize queries on song play analysis, which could make them query the data easier.  The project is to create a database schema and ETL pipeline for this analysis.

---
### Datasets

Song Dataset

The first dataset is a subset of real data from the  [Million Song Dataset](https://labrosa.ee.columbia.edu/millionsong/). Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID.

Log Dataset

The second dataset consists of log files in JSON format generated by this  [event simulator](https://github.com/Interana/eventsim)  based on the songs in the dataset above. These simulate activity logs from a music streaming app based on specified configurations.

---

### Schema for Song Play Analysis
#### Fact Table

1.  **songplays**  - records in log data associated with song plays i.e. records with page  `NextSong`
    -   _songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent_

#### Dimension Tables

2.  **users**  - users in the app
    -   _user_id, first_name, last_name, gender, level_
3.  **songs**  - songs in music database
    -   _song_id, title, artist_id, year, duration_
4.  **artists**  - artists in music database
    -   _artist_id, name, location, latitude, longitude_
5.  **time**  - timestamps of records in  **songplays**  broken down into specific units
    -   _start_time, hour, day, week, month, year, weekday_
    
 ---
  ## Project Steps
 - Create Tables in `sql_queries.py` to create each table. 
 - Run  `create_tables.py`  to create database and tables.
 - Build ETL Processes  in `etl.ipynb` notebook to develop ETL processes for each table. Run `test.ipynb` to confirm that records were successfully inserted into each table.
 - Build ETL Pipeline. Use `etl.ipynb` to complete `etl.py` to process the entire datasets.