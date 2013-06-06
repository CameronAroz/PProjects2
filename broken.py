"""
THIS PROGRAM IS BROKEN!

Part A: Your mission is to:
1. Run the program and take note of the error message.
2. Make a fix to address the error, then add/commit to git. Use
   the error message you were trying to address as your commit message.
3. Run the program again, see if any more error messages come up.
4. Lather, rinse, repeat until you get the output pasted below.
5. Answer the questions in Part B.

Correct output looks like this:

$ python broken.py
I loved this film
I loved this film
I loved this film
I hated this film
['Robert Downey Jr', 'Christian Bale', 'Leonardo Di Caprio']


Part B: Please answer the following questions:
1. Which errors were logical errors, that the Python interpreter caught?
2. Which errors were human errors, that the compiler did not catch?
3. How would I get rid of the 'costar' key from the "Great Gatbsy" dict,
   which I don't want?
4. Write a function that adds the key "year" and the release year to each
   movie dict. (HINT: read the docs for 'dict')
5. Write two functions, each changing the movie name from "Batman"
   to "Batman Begins" in a different way (HINT: read the docs!)
"""

def has_movie_star(movie):
    """Return True if there is a key for a movie star. """
    return movie['star'] is not None

def is_highly_rated(rating):
    """ Return True if the rating is high. """
    threshold = 75
    return rating >= threshold


def main():
    movies_i_like = [
        {'name': 'Iron Man',
         'star': 'Robert Downey Jr'
         'rating': 58},

        {'name': 'Life of Pi'
         'rating': '65'},

        {'name': 'Christian Bale',
         'star': 'Batman',
         'rating': 78},

        {'name': 'The Great Gatsby',
         'Rating': 29,
         'star': 'Leonardo Di Caprio',
         'costar': 'Tobey Maguire'}
    ]

    for movie in movies_i_like:
        if is_highly_rated(movie):
            print 'I loved this film'
        else:
            print 'I hated this film'

	print_movie_star_names(movies_i_like)


def print_movie_star_names(list_of_movies):
    """
    Given a list of movie dicts, return a list of all the movie stars
    TODO: list only existing movie stars (currently this list includes
    values of None)
    """
    movie_stars = []
    for movie in list_of_movies:
        movie_stars.append(movie['star'])
    return movie_stars

main()



