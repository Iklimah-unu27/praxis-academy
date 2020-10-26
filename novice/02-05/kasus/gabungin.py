import psycopg2

conn = psycopg2.connect(database="sample_db", user="dimasutomo", password="", host="127.0.0.1", port = "5432")

cur = conn.cursor()

# print ("Opened database successfully")

# cur.execute('''CREATE TABLE detail_member
#       (
# 			MEMBER_ID 	INT 	PRIMARY KEY 	NOT NULL,
#       FULL_NAMES 	TEXT 	NOT NULL,
#       PHYSICAL_ADDRESS 	CHAR(100),
#       SALUTATION_ID 	INT);''')

# cur.execute('''CREATE TABLE movies_rented
#       (MEMBER_ID 	INT 	PRIMARY KEY 	NOT NULL,
#       MOVIES_RENTED 	TEXT 	NOT NULL);''')

# cur.execute('''CREATE TABLE SALUTATION
#       (SALUTATION_ID 	INT 	PRIMARY KEY 	NOT NULL,
#       SALUTATION 	TEXT 	NOT NULL);''')

# print ("Table created successfully")

# cur.execute("INSERT INTO detail_member (MEMBER_ID, FULL_NAMES, PHYSICAL_ADDRESS, SALUTATION_ID) \
#       VALUES (1, 'Janet Jones', 'First Street Plot No.4', '2')");

cur.execute("SELECT MEMBER_ID, FULL_NAMES, PHYSICAL_ADDRESS, SALUTATION_ID from detail_member")
rows = cur.fetchall()

# for row in rows:
#    print (row[0], 'rents:')

# cur.execute("SELECT MEMBER_ID, MOVIES_RENTED from movies_rented")
# datas = cur.fetchall()

# for data in datas:
# 	print ('1.', data[1])

# conn.commit()

# conn.close()