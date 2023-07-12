class Movie:
	def __init__( self, movie_title, movie_cast, movie_shows, movie_avg_ticket):
		self.movie_title = movie_title
		self.movie_cast = movie_cast
		self. movie_shows = movie_shows
		self. movie_avg_ticket = movie_avg_ticket

	def movieCollections(self):
		return 'The movie collections for ', self.movie_title, ' are ' , self.movie_avg_ticket * self.movie_shows

	
