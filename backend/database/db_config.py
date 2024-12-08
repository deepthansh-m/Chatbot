import psycopg2

def get_connection():
    try:
        connection = psycopg2.connect(
            dbname="chatbot_db",
            user="deepthanshm",
            password="Dimpu@2004",
            host="localhost",
            port=5432
        )
        return connection
    except Exception as e:
        raise Exception(f"Error in database connection: {e}")
