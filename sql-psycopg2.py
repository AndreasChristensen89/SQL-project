import psycopg2


# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database, we need instance of a curser object,
# which is another way of saying a 'set' or 'list'
# lke array in JS. Anything queried from database will be part of cursor object
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
# must use single quotes to wrap the query and double for values
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the "name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only "Queen" from the "Artist" table
# Because the combination of "" and '' is messing things up, we need to use a
# string placeholder %s and then define a list with the desired string
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - select only the albums with with "ArtistId" #51 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - select all tracks where the composer is "Queen" from the "track" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# fetch the results (multiple)
# results = cursor.fetchall()

# fetch the results (single)
results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)
