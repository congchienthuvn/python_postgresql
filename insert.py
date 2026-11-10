import psycopg2

from config import load_config


def insert(vendor_name):
    sql = """INSERT INTO vendors (vendor_name) VALUES (%s) RETURNING vendor_id;"""
    vendor_id = None

    config = load_config(filename='database.ini', section='postgresql')

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (vendor_name,))

                row = cur.fetchone()
                if row:
                    vendor_id = row[0]

                print(f"Thêm thành công nhà cung cấp với ID: {vendor_id}")

    except (Exception, psycopg2.Error) as error:
        print("Lỗi khi thêm dữ liệu:", error)

    return vendor_id

def insert_many (vendor_list):
    sql = "INSERT INTO vendors(vendor_name) VALUES(%s) "
    config = load_config(filename='database.ini', section='postgresql')
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                cur.executemany(sql, vendor_list)
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    insert("3M Co.")
    insert_many([
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
    ])