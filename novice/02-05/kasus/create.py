import psycopg2

def insert_members(records):
    #add records
    members = "INSERT INTO members(member_id, full_names, physical_address, salutation_id) VALUES(%s,%s,%s,%s)"
    conn = None
    try:
        conn = psycopg2.connect(
        database="letsee", 
        user="iklimah", 
#        password="", 
#        host="127.0.0.1", 
        port = "5432") 
        cur = conn.cursor()
        cur.executemany(members, records)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_records_movie_rented(records):
    movie_rented = "INSERT INTO movie_rented(member_id, movies_rented) VALUES(%s, %s)"
    conn = None
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(database="sample_db", user="dimasutomo", password="", host="127.0.0.1", port = "5432") 
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(movie_rented, records)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def insert_records_salutation(records):
    salutation = "INSERT INTO salutation(salutation_id, salutation) VALUES(%s,%s)"
    conn = None
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(database="sample_db", user="dimasutomo", password="", host="127.0.0.1", port = "5432") 
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(salutation, records)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    insert_members([
        (1, 'Janet Jones', 'First Street Plot No.4', 2),
        (2, 'Robert Phil', '3rd Street 34', 1),
        (3, 'Robert', '5th Avenue', 1)
    ])


if __name__ == '__main__':
    insert_records_movie_rented([
        (1, 'Pirates of the Caribbean'),
        (1, 'Clash of the titans'),
        (2, 'Forgetting Sarah Marshal'),
        (2, 'Clash of the Titans')
    ])

if __name__ == '__main__':
    insert_records_salutation([
        (1, 'Mr.'),
        (2, 'Ms.'),
        (3, 'Mrs.'),
        (4, 'Dr.')
    ])