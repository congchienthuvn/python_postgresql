import psycopg2
from config import load_config


def get_vendors():
    config = load_config(filename='database.ini', section='postgresql')

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name")
                rows = cur.fetchall()
                print(f"Tổng số nhà cung cấp tìm thấy: {len(rows)}")

                for row in rows:
                    print(row)

    except (Exception, psycopg2.DatabaseError) as error:
        print("Lỗi khi truy vấn dữ liệu:", error)


if __name__ == '__main__':
    get_vendors()