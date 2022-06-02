from re import X
import psycopg2
from psycopg2 import Error
import time

flag = True

conn = psycopg2.connect(database="postgres",    
                            user="postgres",
                            password="1",
                            host="localhost",
                            port="5432")
cursor = conn.cursor()

X = str(round(time.time()))[7:]

print(Error)
try:
    cursor.execute(f'CREATE SCHEMA a{X}')
    cursor.execute(f'CREATE TABLE a{X}.a{X}\
                (\
                frame varchar(32),\
                id varchar(32),\
                bbox_left varchar(32),\
                bbox_top varchar(32),\
                bbox_w varchar(32),\
                bbox_h varchar(32)\
                );')
    conn.commit()
except (Exception,  Error) as error:
    print(Error)
    flag = False
finally:
    if conn:
        print(flag)
        cursor.close()
        conn.close()
        print("Соединение с PostgreSQL закрыто")