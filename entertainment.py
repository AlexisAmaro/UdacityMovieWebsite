"""Stores details of movies and displays them on a website"""
import fresh_tomatoes
import media

def main():
    """Creates six Movie objects, initialises the objects alongside the title,
    storyline, poster image, video trailer """

shock_treatment = media.Movie("Shock Treatment",
                              "80's game show goes off the rails",
                              "http://bit.ly/2xjpDUR",
                              "https://www.youtube.com/watch?v=z-xRAvVWp5w",
                              )

rocky = media.Movie("Rocky",
                    "The classic movie about an underdog boxer",
                    "http://bit.ly/2jIdIuA",
                    "https://www.youtube.com/watch?v=Wif1EzGQ9Fk",
                    )

hercules = media.Movie("Hercules",
                       "Son of Zeus becomes a god",
                       "http://bit.ly/2xk6L7R",
                       "https://www.youtube.com/watch?v=yIAvF8hFEYM",
                       )

arrival = media.Movie("Arrival",
                      "Aliens show up on earth on strange ships",
                      "http://bit.ly/2wEAcOp",
                      "https://www.youtube.com/watch?v=tFMo3UJ4B4g",
                      )

hocus_pocus = media.Movie("Hocus Pocus",
                          "Witches wake up after thousands of years in salem",
                          "http://bit.ly/2eVrLrA",
                          "https://www.youtube.com/watch?v=2UUMsInka2s",
                           )

space_jam = media.Movie("Space Jam",
                        "Aliens show up to ball against Michael Jordan",
                        "http://bit.ly/2xk18X3",
                        "https://www.youtube.com/watch?v=oKNy-MWjkcU",
                        )
                        
                    
                      
"""Stores movie objects in a list"""                     
movies = [shock_treatment, rocky, hercules, arrival, hocus_pocus, space_jam]
"""Opens the movie website in the browser"""
fresh_tomatoes.open_movies_page(movies)

main()

                    

                     

