import psycopg2
from config import load_config


def add_part(part_name, vendor_name):
    params = load_config(filename='database.ini', section='postgresql')

    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute('CALL add_new_part(%s, %s)', (part_name, vendor_name))

            conn.commit()
            print(f"Đã thêm thành công linh kiện '{part_name}' và nhà cung cấp '{vendor_name}' qua Stored Procedure!")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Lỗi:", error)


if __name__ == '__main__':
    add_part('OLED', 'LG')