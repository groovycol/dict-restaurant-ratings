def create_dict(filename):
    """Return a dictionary and rating score."""

    restaurant_ratings = {}

        #open file and make readable
    working_file = open(filename)

    for line in working_file:
        line = line.rstrip()
        data_in_line = line.split(':')

        restaurant_ratings[data_in_line[0]] = data_in_line[1]

    working_file.close()

    return restaurant_ratings


def print_sorted_data(restaurant_info):
    """Print report of restaurants and ratings alphabetically"""

    for key in sorted(restaurant_info):
        print "{} is rated at {}.".format(key, restaurant_info[key])  


print_sorted_data(create_dict('scores.txt'))