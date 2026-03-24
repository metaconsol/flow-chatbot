import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user= os.getenv("DB_USER"),
        password= os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )







def check_order_in_db(phone):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        print("SEARCHING IN DB:", phone)

        query = """
        SELECT o.id, o.order_no, o.order_status, o.grand_total, o.created_at
        FROM orders o
        JOIN users u ON o.user_id = u.id
        WHERE u.phone_number = %s
        ORDER BY o.created_at DESC
        """

        cursor.execute(query, (phone,))
        result = cursor.fetchone()   # latest order

        print("DB RESULT:", result)

        cursor.close()
        conn.close()

        return result  # None if not found

    except Exception as e:
        print("DB Error:", e)
        return None