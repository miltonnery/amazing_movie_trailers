"""Imports"""
import webbrowser


class Movie():
    """Movie class definition."""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):  # NOQA
        """Instantiates the Movie Class."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens a trailer url in the browser."""
        webbrowser.open(self.trailer_youtube_url)
