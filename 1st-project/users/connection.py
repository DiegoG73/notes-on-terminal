import mysql.connector


def connect():
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        database="fst_app",
        port=3306
    )
    cursor = database.cursor(buffered=True)
    
    return[database, cursor]