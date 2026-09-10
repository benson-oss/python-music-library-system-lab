class Song:
    # Class attributes
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update the class data whenever a song is created
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    def add_song_to_count():
        Song.count += 1

    def add_to_genres(genre):
        Song.genres.add(genre)

    def add_to_artists(artist):
        Song.artists.add(artist)

    def add_to_genre_count(genre):
        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1

    def add_to_artist_count(artist):
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1