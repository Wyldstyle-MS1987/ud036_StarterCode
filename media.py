import webbrowser

# create class Movie to store the tile, poster image URL and a youtube link to the movie trailer of my favorite movies.
class Movie():

# call constructor
    def __init__(self,movie_title,poster_image,trailer_youtube):

# define instance variables movie tile, poster image link and youtube trailer link.
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# define instance method show_trailer, it opens the youtube link to the movie trailer when it is called.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
