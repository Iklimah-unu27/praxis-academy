import psycopg2 

def create_tables(): 

	conn = None
	try: 
		# connect to the PostgreSQL server 
		conn = psycopg2.connect(database="letsee", user="iklimah", host="127.0.0.1", port = "5432") 
		cur = conn.cursor() 
		# create table one by one 
		for table in tables: 
			cur.execute(table)
		# close communication with the PostgreSQL database server 
		cur.close() 
		# commit the changes 
		conn.commit() 

	except (Exception, psycopg2.DatabaseError) as error: 
		print(error) 
	finally: 
		if conn is not None: 
			conn.close()

#run code
if __name__ == '__main__':
	create_tables()