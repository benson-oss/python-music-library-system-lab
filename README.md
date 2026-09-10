# Music Library System

## About the Project

The Music Library System is a Python project that demonstrates how classes, class attributes, and class methods can be used to manage information about songs.

The project is built around a `Song` class. Each song has a name, artist, and genre. In addition to storing information about individual songs, the class keeps track of useful information about the entire music collection.

For example, the system can tell us how many songs have been created, which artists and genres are represented, and how many songs belong to each artist or genre.

This project was created as part of my Object-Oriented Programming (OOP) learning journey.

## Features

The Music Library System can:

- Create a song with a name, artist, and genre.
- Keep track of the total number of songs created.
- Store all unique artists.
- Store all unique genres.
- Count the number of songs for each genre.
- Count the number of songs for each artist.
- Automatically update the library statistics whenever a new song is created.

## Technologies Used

- Python
- Object-Oriented Programming
- Git
- GitHub

## Project Structure

```text
python-music-library-system-lab/
│
├── lib/
│   └── song.py
│
├── README.md
└── ...
How the Song Class Works
The Song class contains three instance attributes:
- name - the name of the song.
- artist - the artist who created the song.
- genre - the genre of the song.
It also contains five class attributes that are shared across all Song objects:
count = 0
genres = set()
artists = set()
genre_count = {}
artists_count = {}
Class Attributes
count
Keeps track of the total number of songs created.
genres
Stores the unique genres found in the music library.
A set is used so that the same genre is not stored multiple times.
artists
Stores the unique artists in the library.
genre_count
Keeps track of how many songs belong to each genre.
For example:
{
    "Pop": 2,
    "Hip-Hop": 1
}
artists_count
Keeps track of how many songs belong to each artist.
For example:
{
    "Ed Sheeran": 1,
    "The Weeknd": 1,
    "Drake": 1
}
Class Methods
The class uses methods to automatically update the library information whenever a new song is created.
add_song_to_count()
Increases the total number of songs by one.
Song.count += 1
add_to_genres(genre)
Adds a genre to the collection of genres.
Because genres is a set, duplicate genres are automatically avoided.
add_to_artists(artist)
Adds an artist to the collection of artists.
The set ensures that an artist is only stored once.
add_to_genre_count(genre)
Updates the number of songs belonging to a particular genre.
If the genre already exists, its count is increased by one. If it does not exist, it is added with a count of one.
add_to_artists_count(artist)
Works in a similar way to add_to_genre_count(), but keeps track of songs for each artist.
Example
Here are some songs created using the Song class:
song1 = Song("Shape of You", "Ed Sheeran", "Pop")
song2 = Song("Blinding Lights", "The Weeknd", "Pop")
song3 = Song("One Dance", "Drake", "Hip-Hop")
When these songs are created, the class automatically updates its statistics.
We can then display the information:


print("Total songs:", Song.count)
print("Genres:", Song.genres)
print("Artists:", Song.artists)
print("Genre counts:", Song.genre_count)
print("Artist counts:", Song.artists_count)
Example Output


```python
Total songs: 3
Genres: {'Pop', 'Hip-Hop'}
Artists: {'Ed Sheeran', 'The Weeknd', 'Drake'}
Genre counts: {'Pop': 2, 'Hip-Hop': 1}
Artist counts: {'Ed Sheeran': 1, 'The Weeknd': 1, 'Drake': 1}

 
 The order of items inside genres and artists may be different because sets are unordered.
Running the Project
1. Clone the repository
git clone git@github.com:benson-oss/python-music-library-system-lab.git
2. Navigate into the project
cd python-music-library-system-lab
3. Open the project in VS Code
code .
4. Run the Python program
If your main file is inside the lib folder:
python3 lib/song.py
The results will be displayed in the terminal.
Git Workflow Used
I used a feature-branch workflow while developing this project.
Create a feature branch
git checkout -b feature/music-library
Check the current branch
git branch
Stage the changes
git add .
Commit the changes
git commit -m "Implement music library system"
Push the feature branch
git push origin feature/music-library
After pushing the branch, I created a Pull Request on GitHub and merged the completed work into main.
Best Practices
While completing the project, I also focused on keeping the code and repository clean.
- Added comments where they help explain the purpose or logic of the code.
- Removed unnecessary and commented-out code.
- Kept the README updated with the current functionality.
- Checked the repository for stale branches.
- Checked .gitignore to make sure unnecessary or sensitive files are not committed.
- Used Git branches and Pull Requests to manage changes.
Screenshot
The screenshot below shows the completed Music Library System running successfully in the terminal.

What I Learned
This project helped me understand how Python classes can be used to manage both individual objects and information shared between those objects.
Some of the main concepts I practiced were:
- Creating classes and objects.
- Using __init__ to initialize objects.
- Understanding instance attributes.
- Understanding class attributes.
- Creating methods that update shared class data.
- Using sets to store unique values.
- Using dictionaries to count values.
- Using .get() when updating dictionary counts.
- Using Git branches and Pull Requests.
- Writing documentation with Markdown.

Future Improvements
There are several features that could be added to make the project more useful as a real music library.
Some possible improvements include:

- Allowing users to add songs through the terminal.
- Adding a method to search for songs.
- Allowing users to search by artist or genre.
- Adding functionality to remove songs.
- Saving the music library to a file or database.
- Building a graphical or web-based interface.

    Author
    Benson Maina
(This project is part of my journey learning Python and Object-Oriented Programming.
)
Also, my GitHub repository is:

`benson-oss/python-music-library-system-lab`

So the clone command should be:

```bash
git clone git@github.com:benson-oss/python-music-library-system-lab.git
