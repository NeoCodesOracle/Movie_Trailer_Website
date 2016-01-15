import webbrowser


class Movie():
    """A class that holds all of our movies information."""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, cast, rating, release_year):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.cast = cast                # Let's add more information to our
        self.rating = rating            # movies by adding the rating of the
        self.released = release_year    # movie and the release year.

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)