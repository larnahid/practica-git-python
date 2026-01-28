import pymysql # Usamos la librería compatible
import sys

print("--- 1. INTENTANDO CONECTAR ---")

try:
    # Conexión directa
    conexion = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="admin1234",      # <--- PRUEBA VACÍA PRIMERO. Si falla, pon tu clave.
        database="inventario",
        port=3306,
        autocommit=True   # Esto ayuda a que los cambios se guarden solos
    )
    
    print("✅ ¡CONEXIÓN EXITOSA! (Usando PyMySQL)")

    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM productos")
        datos = cursor.fetchall()
        
        print(f"📦 Productos en almacén: {len(datos)}")
        for fila in datos:
            print(f" - {fila}")

    conexion.close()

except pymysql.err.OperationalError as e:
    print(f"❌ Error de Acceso: ¿Es posible que la clave no sea esa? \nDetalle: {e}")
except Exception as e:
    print(f"❌ Error General: {e}")

print("--- FIN DEL SCRIPT ---")