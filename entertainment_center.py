import fresh_tomatoes
import media


# These variables store information about the movies.
interstellar = media.Movie("Interstellar",
                           "A crew of astronauts travel through a wormhole in "
                           "search of a new home for humanity.",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")

space_odyssey = media.Movie("2001: A Space Odyssey",
                            "A crew of astronauts investigate the mystery of "
                            "a black obelisk with the help of a sentient "
                            "computer.",
                            "https://upload.wikimedia.org/wikipedia/en/e/ef/2001_A_Space_Odyssey_Style_B.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=3LAi7l3iQuE")

inception = media.Movie("Inception", "A professional theif attempts to redeem "
                        "himself by infiltrating a person's subconscious.",
                        "https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")

pi = media.Movie("Pi", "A loner mathematician discovers the secrets of the "
                       "universe hidden in mathematics.",
                       "https://upload.wikimedia.org/wikipedia/en/5/5a/Piposter.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=jo18VIoR2xU")

the_big_lebowski = media.Movie("The Big Lebowski",
                               "An LA slacker tries to get his rug back.",
                               "https://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",  # NOQA
                               "https://www.youtube.com/watch?v=cd-go0oBF4Y")

office_space = media.Movie("Office Space",
                           "A disillusioned IT worker stops caring about "
                           "his job.",
                           "https://upload.wikimedia.org/wikipedia/en/8/8e/Office_space_poster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=dMIrlP61Z9s")

movies = [interstellar, space_odyssey, inception, pi, the_big_lebowski,
          office_space]

fresh_tomatoes.open_movies_page(movies)
