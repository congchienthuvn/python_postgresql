import psycopg2
from config import load_config


def update_vendor(vendor_id, vendor_name):
    updated_row_count = 0

    sql = """ UPDATE vendors
                SET vendor_name = %s
                WHERE vendor_id = %s """

    # Sửa lại truyền đúng tham số file cấu hình và section
    config = load_config(filename='database.ini', section='postgresql')

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (vendor_name, vendor_id))
                updated_row_count = cur.rowcount

        print(f"Cập nhật thành công! Số dòng bị ảnh hưởng: {updated_row_count}")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Lỗi khi cập nhật dữ liệu:", error)

    return updated_row_count


if __name__ == '__main__':
    update_vendor(1, "3M Corp")