from re import X
import psycopg2
from psycopg2 import Error

conn = psycopg2.connect(database="postgres",
                            user="postgres",
                            password="123456",
                            host="localhost",
                            port="5432")
cursor = conn.cursor()

X = 1
print(Error)
for i in range(X):
    try:
        cursor.execute(f'CREATE SCHEMA shema{X}')
        cursor.execute(f'CREATE TABLE shema{X}.table{X}\
                    (\
                    frame varchar(32),\
                    amount varchar(32),\
                    bbox_left varchar(32),\
                    bbox_top varchar(32),\
                    bbox_w varchar(32),\
                    bbox_h varchar(32)\
                    );')
        conn.commit()
    except (Exception,  Error) as error:
        print(Error)
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Соединение с PostgreSQL закрыто")