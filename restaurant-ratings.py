def create_dict(filename):
    """Return a dictionary of restaurants and rating score."""

    restaurant_ratings = {}

    with open(filename) as working_file:

        for line in working_file:
            line = line.rstrip()
            data_in_line = line.split(':')

            restaurant_ratings[data_in_line[0]] = data_in_line[1] 

    return restaurant_ratings


def add_user_ratings(restaurant_info):
    """Add new key value pair to the dictionary passed in. Return updated dictionary."""

    user_rest = raw_input("Please enter a restaurant name: ")
    while True: 
        try:
            user_rating = int(raw_input("Please enter a rating for {}: ".format (user_rest)))
            break
        except ValueError:
            print "Oops! That was not a valid number Try again..."

    restaurant_info[user_rest] = user_rating

    return restaurant_info


def print_sorted_data(restaurant_info):
    """Print report of restaurants and ratings alphabetically"""

    for key in sorted(restaurant_info):
        print "{} is rated at {}.".format(key, restaurant_info[key])  



restaurant_dictionary = create_dict('scores.txt')

print_sorted_data(add_user_ratings(restaurant_dictionary))