#Name - Parul Nagar
#Section - Data Science MSc
#Description - The program defines the class `Supplier`, which represents the supplier that are available for restocking supplies, 
#along with the their pricing for the supplies per unit.

class Supplier:
    """
    Supplier class representing the suppliers.
    """
    def __init__(self, name, fertilizer_rate, feed_rate, salt_rate):
        """
        Initializes a supplier with the required attributes.
        Parameters:
        name (str) - the name of the supplier
        fertilizer_rate (float) - the rate for the fertilizer by the supplier
        feed_rate (float) - the rate for the feed by the supplier
        salt_rate (float) - the rate for the salt by the supplier
        """
        self.name = name    #name of the supplier
        self.fertilizer_rate = fertilizer_rate  #rate of fertilizer by the supplier
        self.feed_rate = feed_rate     #rate of feed by the supplier
        self.salt_rate = salt_rate     # #rate of salt by the supplier
