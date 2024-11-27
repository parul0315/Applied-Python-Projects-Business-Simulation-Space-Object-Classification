#Name - Parul Nagar
#Section - Data Science MSc
#Description - The program defines a class `Fish`. The `Fish` class models a fish type's attributes for the hatchery. 

class Fish:
    """ 
    initializing the fish class with the required attributes, 
    which are the name of the fish type, fertilizer required, feed required, 
    salt required, time takes for maintaning the fish, demand of the fish type and the price of each fish. 
    """
    def __init__(self, name, fertilizer, feed, salt, time, demand, price):
        self.name = name    #name of the fish
        self.fertilizer = fertilizer    #the amount of fertilizer needed for the fish
        self.feed = feed    #the amount of feed needed
        self.salt = salt    #the amount of salt needed
        self.time = time / 5    #the time required to harvest each fish (in weeks)
        self.price = price     #the price of each fish
        self.demand = demand    #the demand of each fish per quarter

# Requirements of each species along with the demand and price.
# fish_type = [
#         ("Clef Fins", 100.0, 12, 2, 2.0, 25, 250),
#         ("Timpani Snapper", 50.0, 9, 2, 1.0, 10, 350),
#         ("Andalusian Brim", 90.0, 6, 2, 0.5, 15, 250),
#         ("Plagal Cod", 100.0, 10, 2, 2.0, 20, 400),
#         ("Fugue Flounder", 200.0, 12, 2, 2.5, 30, 550),
#         ("Modal Bass", 300.0, 12, 6, 3.0, 50, 500)
#     ]