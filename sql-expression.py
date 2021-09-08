from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, MetaData
)

# executing the instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# We need to define all the tables before we can use them
# create variable for "Artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# create variable for "Album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
    # With foregin need to tell where to find the table, refer to above
)

# create variable for "track" table
track_tble = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    # Technically a foreign key, but this lesson we don't define all,
    # only the ones we need
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# make the connection
with db.connect() as connection:
    # Query 1 - select all records from the "Artist" table
    select_query = artist_table.select()

    results = connection.execute(select_query)
    for result in results:
        print(result)
