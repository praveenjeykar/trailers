#!/usr/bin/env python
import media
import fresh_tomatoes
print("Content-type:text/html \r\n\r\n")
blueroses = media.Movie("Blue Roses", "https://bit.ly/2kazWmh",
                        "https://www.youtube.com/embed/eoJxaz3VtuE")
kingfisher = media.Movie("Kingfisher", "https://bit.ly/2IWI1ZP",
                         "https://www.youtube.com/embed/Egjmby3wayQ")
pets = media.Movie("Randy", "https://bit.ly/2Iyg0IF",
                   "https://www.youtube.com/embed/CKMNMsRaWLI")
fish = media.Movie("Nemo", "https://bit.ly/2LgVo5m",
                   "https://www.youtube.com/embed/XcQqm7LNRFY")
movies = [blueroses, kingfisher, pets, fish]
fresh_tomatoes.open_movies_page(movies)

