import webbrowser


class Movie():
    
    #Movie class definition
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
        
    #Opens a trailer url in the browser    
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)