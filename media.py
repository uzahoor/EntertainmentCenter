import webbrowser


# A class used to represent a movie
class Movie():
    """ This class provides a way to store movie related information

    Attributes:
        movie_title (str): The title of the movie.
        movie_storyline (str): A short synopsys of the movie.
        poster_image (str): A URL to an image file of the movie poster.
        trailer_youtube (str): A URL to a youtube video of the movie trailer.

    """
    __name__ = "Movie"
    __module__ = "media"

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """ This function initializes a instance of the Movie class

        Args:
            movie_title (str): The title of the movie.
            movie_storyline (str): A short synopsys of the movie.
            poster_image (str): A URL to an image file of the movie poster.
            trailer_youtube (str): A URL to a youtube video of the movie
                trailer.

        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
