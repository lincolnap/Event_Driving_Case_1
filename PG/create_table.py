import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv,dotenv_values
import os
load_dotenv()


db_config = {
    "dbname": "streaming",  
    "user": f"{os.getenv("POSTGRES_USER")}",       
    "password": f"{os.getenv("POSTGRES_PASSWORD")}", 
    "host": "localhost",         
    "port": "5432"               
}


create_table_query = """
CREATE TABLE IF NOT EXISTS clients (
    id serial PRIMARY KEY,
    name VARCHAR(200),
    location VARCHAR(10000),
    phone VARCHAR
);
"""

# Conexión y ejecución de la sentencia
try:
    # Conectar a la base de datos
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    # Ejecutar la sentencia SQL
    cursor.execute(create_table_query)
    conn.commit()

    print("Tabla 'clients' creada exitosamente.")

except Exception as e:
    print(f"Error al crear la tabla: {e}")

finally:
    # Cerrar conexión
    if cursor:
        cursor.close()
    if conn:
        conn.close()
