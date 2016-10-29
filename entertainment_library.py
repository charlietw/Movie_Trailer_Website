import fresh_tomatoes  # for the HTML formatting and built in python functions
import media  # to define the Movie class

Toy_Story = media.Movie("Toy Story",
                        "A cowboy doll is profoundly threatened and jealous"
                        " when a new spaceman figure supplants him as top toy"
                        " in a boy's room.",
                        "http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "1h 21m")

Gladiator = media.Movie("Gladiator",
                        "When a Roman general is betrayed and his family"
                        " murdered by an emperor's corrupt son, he comes to"
                        " Rome as a gladiator to seek revenge.",
                        "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=ol67qo3WhJk",
                        "2h 35m")

Whiplash = media.Movie("Whiplash",
                       "A promising young drummer enrolls at a cut-throat"
                       " music conservatory where his dreams of greatness"
                       " are mentored by an instructor who will stop at"
                       " nothing to realize a student's potential.",
                       "https://mattmulcahey.files.wordpress.com/2015/01/whiplash-poster-cold-open-is-firm-dont-know-artist1.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=7d_jQycdQGo",
                       "1h 47m")

Inglourious_Basterds = media.Movie("Inglourius Basterds",
                                   "In Nazi-occupied France during World"
                                   " War II, a plan to assassinate Nazi"
                                   " leaders by a group of Jewish U.S."
                                   " soldiers coincides with a theatre"
                                   " owner's vengeful plans for the same.",
                                   "https://www.uphe.com/sites/default/files/styles/scale__344w_/public/025192014277_DVD_2D-X.png?itok=KgJfTnWH",  # NOQA
                                   "https://www.youtube.com/watch?v=KnrRy6kSFF0",  # NOQA
                                   "2h 33m")

Trainspotting = media.Movie("Trainspotting",
                            "Renton, deeply immersed in the Edinburgh drug"
                            " scene, tries to clean up and get out, despite"
                            " the allure of the drugs and influence of"
                            " friends.",
                            "http://img.goldposter.com/2015/04/Trainspotting_poster_goldposter_com_9.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=R2GKVtWsXKY",
                            "1h 34m")

The_Departed = media.Movie("The Departed",
                           "An undercover cop and a mole in the police attempt"
                           " to identify each other while infiltrating an"
                           " Irish gang in South Boston.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMTI1MTY2OTIxNV5BMl5BanBnXkFtZTYwNjQ4NjY3._V1_SX640_SY720_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=iojhqm0JTW4",
                           "2h 31m")

# Creating the list of movies to pass to the "open_movies_page" function.
movies_list = [
    Toy_Story, Gladiator, Whiplash,
    Inglourious_Basterds, Trainspotting, The_Departed
    ]

# Calling the function to open the browser populated with the list of movies
fresh_tomatoes.open_movies_page(movies_list)
