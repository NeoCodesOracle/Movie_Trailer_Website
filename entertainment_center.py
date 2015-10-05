import fresh_tomatoes
import media

# This is where we build our list of movies to be used in our exercise.
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",   # noqa
                        "https://youtu.be/4KPTXpQehio?t=6s",
                        "Tom Hanks, Tim Allen, Don Rickles",
                        "G",
                        "1995")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # noqa
                     "https://youtu.be/5PSNL1qE6VY?t=2m17s",
                     "Sam Worhtington, Stephen Lang, Sigourney Weaver",
                     "PG-13",
                     "2009")

guardians = media.Movie("Guardians of the Galaxy",
                        "An unlikely group of superheroes step up \
                         to the challenge.",
                        "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",  # noqa
                        "https://youtu.be/crIaEzXgqto?t=39s",
                        "Chris Pratt, Zoe Saldana, Dave Bautista",
                        "PG-13",
                        "2014")

shawshank = media.Movie("Shawshank Redemption",
                        "Andy Dufresne, a banker who is sentenced to life in \
                        Shawshank State Prison for the murder of his wife\
                        and her lover despite his claims of innocence.",
                        "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",  # noqa
                        "https://youtu.be/6hB3S9bIaco?t=18s",
                        "Tim Robbins, Morgan Freeman, Paul Newman",
                        "R",
                        "1994")

inception = media.Movie("Inception",
                     "Your mind is the scene of the crime",
                     "https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",  # noqa
                     "https://youtu.be/8hP9D6kZseM?t=7s",
                     "Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page",
                     "PG-13",
                     "2010")

matrix = media.Movie("The Matrix",
                     "A dystopian future in which reality as perceived by most \
                     humans is actually a simulated reality called created by \
                     sentient machines to subdue the human population, while \
                     their bodies' heat and electrical activity are used as\
                     an energy source.",
                     "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",  # noqa
                     "https://youtu.be/m8e-FF8MsqU?t=38s",
                     "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss",
                     "R",
                     "1999")

notebook = media.Movie("The Notebook",
                        "A Local country boy Noah Calhoun (Ryan Gosling) is \
                        smitten with seventeen-year-old heiress Allie Hamilton\
                        (Rachel McAdams) after seeing her at a carnival, and\
                        they share an idyllic summer love affair.",
                        "https://upload.wikimedia.org/wikipedia/en/8/86/Posternotebook.jpg",  # noqa
                        "https://youtu.be/yDJIcYE32NU",
                        "Ryan Gosling, Rachel McAdams, James Garner",
                        "PG-13",
                        "2004")

enemy = media.Movie("Enemy of the State",
                     "U.S. National Security Agency agents conspiring to kill \
                     a U.S. Congressman and try to cover up the murder.",
                     "https://upload.wikimedia.org/wikipedia/en/7/75/Enemy_of_the_State.jpg",  # noqa
                     "https://youtu.be/MJQ30fPYec8?t=9s",
                     "Will Smith, Gene Hackman, Jon Voight",
                     "R",
                     "1998")

hangover = media.Movie("The Hangover",
                     "Best friends get into all kinds of adventures following \
                     a bachelor party that takes place in Vegas.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b9/Hangoverposter09.jpg",  # noqa
                     "https://youtu.be/tcdUhdOlz9M?t=7s",
                     "Bradley Cooper, Ed Helms, Zack Galifianakis",
                     "R",
                     "2009")

# Let's put our movies in a list and call it movies
movies = [toy_story, avatar, guardians, shawshank, inception,
          matrix, notebook, enemy, hangover]

# Give the list to the function open_movies found in fresh_tomatoes module
fresh_tomatoes.open_movies_page(movies)
