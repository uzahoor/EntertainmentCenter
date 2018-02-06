import media  # flake8: noqa
import fresh_tomatoes

# Create empty array of Movies to be passed to open_movies_page()
movies = []

# Create and add "Godfather Part Two" instance of Movie to movies array
god_father_two = media.Movie("The Godfather Part II",
                             "All the power on earth can't change destiny.",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BMjZiNzIxNTQtNDc5Zi00YWY1LThkMTctMDgzYjY4YjI1YmQyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,702,1000_AL_.jpg",
                             "https://www.youtube.com/watch?v=8PyZCU2vpi8")
movies.append(god_father_two)

# Create and add "Goodfellas" instance of Movie to movies array
goodfellas = media.Movie("Goodfellas",
                         "Shooting people was 'No big deal'.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BNThjMzczMjctZmIwOC00NTQ4LWJhZWItZDdhNTk5ZTdiMWFlXkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_CR0,0,669,1000_AL_.jpg",
                         "https://www.youtube.com/watch?v=qo5jJpHtI1Y")
movies.append(goodfellas)

# Create and add "LOTR: Two Towers" instance of Movie to movies array
lotr_two_towers = media.Movie("LOTR: The Two Towers",
                              "A New Power Is Rising.",
                              "https://images-na.ssl-images-amazon.com/images/M/MV5BMDY0NmI4ZjctN2VhZS00YzExLTkyZGItMTJhOTU5NTg4MDU4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg",
                              "https://www.youtube.com/watch?v=2dlRvAjU_RI")
movies.append(lotr_two_towers)

# Create and add "Dark Knight Rises" instance of Movie to movies array
dark_knight_rises = media.Movie("The Dark Knight Rises",
                                "Rise",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk4ODQzNDY3Ml5BMl5BanBnXkFtZTcwODA0NTM4Nw@@._V1_.jpg",
                                "https://www.youtube.com/watch?v=g8evyE9TuYk")
movies.append(dark_knight_rises)

# Create and add "The Matrix" instance of Movie to movies array
the_matrix = media.Movie("The Matrix",
                         "Welcome to the Real World",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,665,1000_AL_.jpg",
                         "https://www.youtube.com/watch?v=m8e-FF8MsqU")
movies.append(the_matrix)

# Create and add "Super Troopers" instance of Movie to movies array
super_troopers = media.Movie("Super Troopers",
                             "Altered State Police",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BYzAyOTZjZDItZjNiYy00YTA3LWEyYWMtZTA0NmUzYjZhNjg0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
                             "https://www.youtube.com/watch?v=2-9D2qUHN-E")
movies.append(super_troopers)

# Pass movies array to open_movies_page to create html document with movies
fresh_tomatoes.open_movies_page(movies)
