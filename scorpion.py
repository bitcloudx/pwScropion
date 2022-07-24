import psycopg2
import traceback
import bcrypt


def log_info(url_link, password, username, email, app_name):
    try:
        login_info = open('info.txt', 'r')
        data = login_info.read()
        split_data = data.split('\n')
        conn = None
        cursor = None

        conn = psycopg2.connect(
            f"dbname={split_data[0]} user={split_data[1]} host='127.0.0.1' password={split_data[3]}")
        cursor = conn.cursor()
        postgres_insert = """INSERT INTO account_information (url_link, password, username, email, app_name) VALUES(%s, %s, %s, %s, %s)"""
        cursor.execute(postgres_insert, record_to_insert)
        conn.commit()
        cursor.close()
        conn.close()
    except psycopg2.Error as e:
        print("I am unable to connect to the database")
        print(e.pgcode)
        print(e.pgerror)
        print(traceback.format_exc())
    finally:
        if conn != None:
            cursor.close()
            conn.close()
