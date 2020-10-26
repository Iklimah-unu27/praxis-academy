import psycopg2

#connect to database
conn = psycopg2.connect(database="sample_db", user="dimasutomo", password="", host="127.0.0.1", port = "5432")

cur = conn.cursor()

cur.execute("SELECT full_names FROM members")
rows = cur.fetchone()

#fetch first rows
cur.execute("SELECT movies_rented FROM movie_rented OFFSET 0 ROWS FETCH FIRST 1 ROWS only;")
movies = cur.fetchall()

#fetch second rows
cur.execute("SELECT movies_rented FROM movie_rented OFFSET 1 ROWS FETCH FIRST 1 ROWS only;")
movies_2 = cur.fetchall()

#show member name first row
print (rows[0], 'rents:')

#show member name first row
for movie in movies:
	print('1.', movie[0])

for movie in movies_2:
	print('2.', movie[0])

conn.commit()
conn.close()