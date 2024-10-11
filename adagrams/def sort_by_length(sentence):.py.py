restaurants = [{"name": "Grillby's", "rating": 1}, {"name": "Crow's Nest", "rating": 5},{"name": "Flanagan's", "rating": 7}]

def get_highest_rated(restaurants):
    highest_rated = []
    i = 0
    if not restaurants:
        return None
    if len(restaurants) == 1:
        highest_rated = restaurants[0]
    for restaurant in restaurants:
        if len(highest_rated) == 0:
            highest_rated = restaurants[0]
            i += 1
        elif restaurant["rating"] > highest_rated["rating"]:
            highest_rated = restaurants[i]
            i += 1
        

    print(highest_rated)

get_highest_rated(restaurants)

