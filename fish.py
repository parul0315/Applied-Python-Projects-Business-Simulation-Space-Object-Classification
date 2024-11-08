class Fish:
    """ 
    initializing the fish class with the required attributes. 
    """
    def __init__(self, name, fertilizer, feed, salt, time, demand, price):
        self.name = name
        self.fertilizer = fertilizer
        self.feed = feed
        self.salt = salt
        self.time = time
        self.price = price
        self.demand = demand

# Requirements of each species along with the demand and price.
# fish_type = [
#         ("Clef Fins", 100.0, 12, 2, 2.0, 25, 250),
#         ("Timpani Snapper", 50.0, 9, 2, 1.0, 10, 350),
#         ("Andalusian Brim", 90.0, 6, 2, 0.5, 15, 250),
#         ("Plagal Cod", 100.0, 10, 2, 2.0, 20, 400),
#         ("Fugue Flounder", 200.0, 12, 2, 2.5, 30, 550),
#         ("Modal Bass", 300.0, 12, 6, 3.0, 50, 500)
#     ]