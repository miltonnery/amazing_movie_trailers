"""Imports"""
import movie_trailers
import media

# Instances creation

# Interestellar Movie:
# movie title, storyline, poster image and movie trailer
interstellar = media.Movie(
    "Interstellar",
    "A team of explorers travel through a wormhole in space in an attempt "
    "to ensure humanity's survival.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SY1000_CR0,0,640,1000_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=zSWdZVtXT7E")

# Guardians of the Galaxy (Vol 2) Movie:
# movie title, storyline, poster image and movie trailer
guardians_of_the_galaxy = media.Movie(
    "Guardians of the Galaxy 2",
    "The Guardians must fight to keep their newfound family "
    "together as they unravel the mystery of Peter Quill's true parentage.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg2MzI1MTg3OF5BMl5BanBnXkFtZTgwNTU3NDA2MTI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=duGqrYw4usE")

# Iron Man Three Movie:
# movie title, storyline, poster image and movie trailer
iron_man_three = media.Movie(
    "Iron Man 3",
    "When Tony Stark's world is torn apart by a formidable terrorist "
    "called the Mandarin, he starts an odyssey of rebuilding and retribution.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkzMjEzMjY1M15BMl5BanBnXkFtZTcwNTMxOTYyOQ@@._V1_SY1000_SX700_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=Ke1Y3P9D0Bc")

# Thor Ragnarok Movie:
# movie title, storyline, poster image and movie trailer
thor_ragnarok = media.Movie(
    "Thor Ragnarok",
    "Imprisoned, the mighty Thor finds himself in a lethal "
    "gladiatorial contest against the Hulk, his former ally. "
    "Thor must fight for survival and race against time to "
    "prevent the all-powerful Hela from destroying his home "
    "and the Asgardian civilization.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjMyNDkzMzI1OF5BMl5BanBnXkFtZTgwODcxODg5MjI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=ue80QwXMRHg")

# Capitain America (Civil War) Movie:
# movie title, storyline, poster image and movie trailer
capitain_america = media.Movie(
    "Capitain America: Civil War",
    "Political interference in the Avengers' activities"
    "causes a rift between former allies Captain America and Iron Man.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQ0MTgyNjAxMV5BMl5BanBnXkFtZTgwNjUzMDkyODE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=dKrVegVI0Us")

# Deadpool Movie:
# movie title, storyline, poster image and movie trailer
deadpool = media.Movie(
    "Deadpool",
    "A fast-talking mercenary with a morbid sense of humor is "
    "subjected to a rogue experiment that leaves him with accelerated "
    "healing powers and a quest for revenge.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQyODg5Njc4N15BMl5BanBnXkFtZTgwMzExMjE3NzE@._V1_SY1000_SX686_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=0JnRdfiUMa8")

# Generating array of instances created
movies = [interstellar,
          guardians_of_the_galaxy,
          iron_man_three,
          thor_ragnarok,
          capitain_america,
          deadpool]

# Creating web page
movie_trailers.open_movies_page(movies)
