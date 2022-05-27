import psycopg2

try:
    conn = psycopg2.connect(dbname='postgres', user='alex',
                            password='1234', host='localhost')
    with conn.cursor() as cursor:
        # cursor.execute(
        #    'SELECT * FROM "public.detect";'
        # )
        cursor.execute(
            'SELECT frame_idx, id, bbox_left, bbox_top, bbox_w, bbox_h FROM "public.detect";')

        # fetching the rows from the cursor object
        result = cursor.fetchall()

        print("frame_idx, id, bbox_left, bbox_top, bbox_w, bbox_h")
        for row in result:
            print("%s, %s, %s, %s, %s, %s" %
                  (row[0], row[1], row[2], row[3], row[4], row[5]))

        # print(cursor.fetchall())
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if conn:
        conn.close()
        print("[INFO] PostgreSQL connection close")
