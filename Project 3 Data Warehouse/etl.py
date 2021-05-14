import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    Load data files from S3 to created staging tables in sql queries file
    param
    cur: database cursor
    conn: database connector
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    Insert stored file data to staging tables and create dimensional tables
    Excute insert queries in sql queries file
    param
    cur: database cursor
    conn: database connector
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
     - Establishes connection with S3 data and gets cursor to it.  
    
     - Drops all the tables.  
    
     - Creates all tables needed. 
    
     - Finally, closes the connection. 
     """
    
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()