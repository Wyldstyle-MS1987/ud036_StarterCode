import media
import fresh_tomatoes

"""Create six instances of class Movie from module media.py.
Each instance has three variables including title,
poster image link and youtube movie trailer link.
"""


La_La_Land = media.Movie("La La Land", "https://upload.wikimedia.org/"
                         "wikipedia/en/a/ab/La_La_Land_%28film%29.png",
                         "https://www.youtube.com/watch?v=C39YJymGp3Q"
                         "&list=PL86F4D497FD3CACCE&index=13")

The_Social_Network = media.Movie("The Social Network", "https://upload"
                                 ".wikimedia.org/wikipedia/en/7/7a/Social_"
                                 "network_film_poster.jpg", "https://www.you"
                                 "tube.com/watch?v=ku5LEcgpvFM&list=PL86F4D497"
                                 "FD3CACCE&index=14")

The_Princess_Bride = media.Movie("The Princess Bride", "https://images-na.ssl"
                                 "-images-amazon.com/images/I/81nq1uq4wyL._SY"
                                 "445_.jpg", "https://www.youtube.com/watch?v"
                                 "=E28KDhsJ65U&list=PL"
                                 "86F4D497FD3CACCE&index=29")

Big_Hero_6 = media.Movie("Big Hero 6", "https://images-na.ssl-images-amazon."
                         "com/images/M/MV5BMDliOTIzNmUtOTllOC00NDU3LWFiNjYt"
                         "MGM0NDc1YTMxNjYxXkEyXkFqcGdeQXVyNTM3NzExMDQ@._V1_"
                         "SY1000_CR0,0,699,1000_AL_.jpg", "https://www.you"
                         "tube.com/watch?v=ihCciBFdbkw&list="
                         "PL86F4D497FD3CACCE&index=55")

Mad_Max_Fury_Road = media.Movie("Mad Max: Fury Road", "https://resizing.f"
                                "lixster.com/8Nvzcr-cC15EDx3qPrR_bFa0OLo"
                                "=/206x305/v1.bTsxMTE5MTI3NjtqOzE3NDU0O"
                                "zEyMDA7NTA5Ozc1NQ", "https://www.youtu"
                                "be.com/watch?v=0RXhcqdewf0&list=PL86"
                                "F4D497FD3CACCE&index=99")

The_Fault_In_Our_Stars = media.Movie("The Fault In Our Stars",
                                     "https://upload.wikimedia.org/wik"
                                     "ipedia/en/4/41/The_Fault_in_Our_St"
                                     "ars_%28Official_Film_Poster%29.png",
                                     "https://www.youtube.com/watch?v=4"
                                     "hKpOi09qqE&list=PL86F4D497FD"
                                     "3CACCE&index=141")

# Group six instances together in a list called "movies".
movies = [La_La_Land, The_Social_Network, The_Princess_Bride,
          Big_Hero_6, Mad_Max_Fury_Road, The_Fault_In_Our_Stars]

"""Call function open_movies_page from module fresh_tomatoes.py.
The function will create an HTML file to display the six movies
in the list "movies".
Click on the image of one of the movies in the HTML file,
it will play the movie trailer in youtube.
"""
fresh_tomatoes.open_movies_page(movies)
