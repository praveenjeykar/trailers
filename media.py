#!/usr/bin/env python
import webbrowser


class Movie():
    '''
    class Movie():
         Attributes:
               movie_title (str): displays the title of the movie.
                poster_image (str): one of the look as image.
                trailer_youtube (str): url of the youtube trailer of the movie.
    '''
# We have taken a function which accepts four given arguments.
    def __init__(self, movie_title, poster_image, trailer_youtube):
                self.title = movie_title
                self.poster_image_url = poster_image
                self.trailer_youtube_url = trailer_youtube


def show_trailer(self):
            webbrowser.open(self.trailer_youtube_url)
