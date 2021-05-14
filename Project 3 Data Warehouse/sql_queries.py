import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS user"
song_table_drop = "DROP TABLE IF EXISTS song"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

staging_events_table_create= ("""CREATE TABLE IF NOT EXISTS staging_events(
    artist              VARCHAR(MAX),
    auth                VARCHAR,
    firstName           VARCHAR,
    gender              VARCHAR,
    itemInSession       INTEGER,
    lastName            VARCHAR,
    length              FLOAT,
    level               VARCHAR,
    location            VARCHAR,
    method              VARCHAR,
    page                VARCHAR,
    registration        FLOAT,
    sessionId           INTEGER,
    song                VARCHAR,
    status              INTEGER,
    ts                  BIGNIT,
    userAgent           VARCHAR,
    userId              INTEGER 
)""")

staging_songs_table_create = ("""CREATE TABLE IF NOT EXISTS staging_songs(
    num_songs           INTEGER,
    artist_id           VARCHAR,
    artist_latitude     FLOAT,
    artist_longitude    FLOAT,
    artist_location     VARCHAR,
    artist_name         VARCHAR,
    song_id             VARCHAR,
    title               VARCHAR,
    duration            FLOAT,
    year                INTEGER
)""")

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplay(
    songplay_id         INTEGER         IDENTITY(0,1)   PRIMARY KEY SORTKEY,
    start_time          TIMESTAMP,       
    user_id             INTEGER         NOT NULL DISTKEY,
    level               VARCHAR,
    song_id             VARCHAR,     
    artist_id           VARCHAR,         
    session_id          INTEGER,
    location            VARCHAR,
    user_agent          VARCHAR
    
)""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS user(
    user_id             INTEGER         NOT NULL PRIMARY KEY DISTKEY,
    first_name          VARCHAR,
    last_name           VARCHAR,
    gender              VARCHAR,     
    level               VARCHAR     
    
)""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS song(
    song_id     VARCHAR PRIMARY KEY,
    title       VARCHAR,
    artist_id   VARCHAR DISTKEY,
    year        INTEGER,
    duration    FLOAT

)""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artist(
    artist_id          VARCHAR PRIMARY KEY DISTKEY,
    name               VARCHAR,
    location           VARCHAR,
    latitude           FLOAT,
    longitude          FLOAT

)""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time(
    start_time    TIMESTAMP PRIMARY KEY DISTKEY SORTKEY,
    hour          INTEGER,
    day           INTEGER,
    week          INTEGER,
    month         INTEGER,
    year          INTEGER,
    weekday       INTEGER

)""")

# STAGING TABLES

staging_events_copy = ("""
    COPY staging_events FROM {}
    CREDENTIALS 'aws_iam_role={}'
    COMPUPDATE OFF REGION 'us-west-2'
    TIMEFORMAT AS 'epochmillisecs'
    FORMAT AS JSON {};
""").format(config.get('S3', 'LOG_DATA'), config.get('IAM_ROLE', 'ARN'), config.get('S3', 'LOG_JSONPATH'))

staging_songs_copy = ("""
    COPY staging_songs FROM {}
    CREDENTIALS 'aws_iam_role={}'
    COMPUPDATE OFF REGION 'us-west-2'
    FORMAT AS JSON 'auto';
""").format(config.get('S3', 'SONG_DATA'), config.get('IAM_ROLE', 'ARN'))

# FINAL TABLES

songplay_table_insert = ("""
INSERT INTO songplay (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
SELECT  DISTINCT(e.ts)      AS start_time, 
            e.userId        AS user_id, 
            e.level         AS level, 
            s.song_id       AS song_id, 
            s.artist_id     AS artist_id, 
            e.sessionId     AS session_id, 
            e.location      AS location, 
            e.userAgent     AS user_agent
    FROM staging_events AS e
    JOIN staging_songs  AS s   
    ON (e.song = s.title AND e.artist = s.artist_name)
    WHERE e.page  =  'NextSong'
""")

user_table_insert = ("""
INSERT INTO user (user_id, first_name, last_name, gender, level)
SELECT  DISTINCT(userId)    AS user_id,
            firstName       AS first_name,
            lastName        AS last_name,
            gender,
            level
    FROM staging_events
    WHERE user_id IS NOT NULL
    AND page  = 'NextSong';
""")

song_table_insert = ("""
INSERT INTO song (song_id, title, artist_id, year, duration)
SELECT  DISTINCT(song_id) AS song_id,
            title,
            artist_id,
            year,
            duration
    FROM staging_songs
    WHERE song_id IS NOT NULL;
""")

artist_table_insert = ("""
INSERT INTO artist (artist_id, name, location, latitude, longitude)
SELECT  DISTINCT(artist_id) AS artist_id,
        artist_name         AS name,
        artist_location     AS location,
        artist_latitude     AS latitude,
        artist_longitude    AS longitude
    FROM staging_songs
    WHERE artist_id IS NOT NULL;
""")

time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
SELECT  DISTINCT(start_time)                AS start_time,
        EXTRACT(hour FROM start_time)       AS hour,
        EXTRACT(day FROM start_time)        AS day,
        EXTRACT(week FROM start_time)       AS week,
        EXTRACT(month FROM start_time)      AS month,
        EXTRACT(year FROM start_time)       AS year,
        EXTRACT(dayofweek FROM start_time)  as weekday
    FROM songplays;
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
