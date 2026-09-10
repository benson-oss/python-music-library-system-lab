class Song:
    # Class attributes
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artists_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)
        
    def add_song_to_count():
        Song.count += 1

    def add_to_genres(genre):
        Song.genres.add(genre)
       
    def add_to_artists(artist):
        Song.artists.add(artist)
        
    def add_to_genre_count(genre):
        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1

    def add_to_artists_count(artist):
        Song.artists_count[artist] = Song.artists_count.get(artist, 0) + 1

song1 = Song("Shape of You", "Ed Sheeran", "Pop")
song2 = Song("Blinding Lights", "The Weeknd", "Pop")
song3 = Song("One Dance", "Drake", "Hip-Hop")

print("Total songs:", Song.count)
print("Genres:", Song.genres)
print("Artists:", Song.artists)
print("Genre counts:", Song.genre_count)
print("Artist counts:", Song.artists_count) 