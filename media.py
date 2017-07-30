import webbrowser

"""Create class Movie to store the tile, poster image URL and
a youtube link to the movie trailer of my favorite movies.
"""


class Movie():
    # Call constructor
    def __init__(self, movie_title, poster_image, trailer_youtube):
        """Define instance variables movie tile,
        poster image link and youtube trailer link.
        """
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    """Define instance method show_trailer.
    It opens the youtube link to the movie trailer when it is called.
    """
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
