class Video():
    def __init__(self, title, storyline):
        """An overarching class for all forms of video media.
        Inputs are title & storyline.
        """
        self.title = title
        self.movie_storyline = storyline


class Movie(Video):
    def __init__(self, title, storyline,
                 poster_image, trailer_youtube, runtime):
        """Specifically for movies, adding poster, trailer & runtime."""
        Video.__init__(self, title, storyline)
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.movie_runtime = runtime
