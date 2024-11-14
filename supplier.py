class Supplier:
    """
    Supplier class representing the suppliers
    """
    def __init__(self, name, fertilizer_rate, feed_rate, salt_rate):
        self.name = name 
        self.fertilizer_rate = fertilizer_rate
        self.feed_rate = feed_rate  #the rate of salt and feed is in grams
        self.salt_rate = salt_rate
